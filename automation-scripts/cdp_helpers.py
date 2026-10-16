import socket, base64, json, struct

def get_ws():
    import subprocess
    out = subprocess.check_output(["curl","-s","http://127.0.0.1:9222/json/list"])
    pages = json.loads(out)
    for p in pages:
        if p.get("type") == "page" and "politeknikkirana" in p.get("url",""):
            return p["id"]
    return pages[0]["id"]

class CDP:
    def __init__(self, page_id, host="127.0.0.1", port=9222):
        self.host, self.port = host, port
        path = f"/devtools/page/{page_id}"
        key = base64.b64encode(b"0123456789abcdef").decode()
        req = (f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
               f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n")
        self.sock = socket.create_connection((host, port), timeout=10)
        self.sock.sendall(req.encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            chunk = self.sock.recv(4096)
            if not chunk: break
            buf += chunk
        self.leftover = buf[buf.find(b"\r\n\r\n")+4:]
        self._id = 0

    def _send_frame(self, payload, opcode=0x1):
        fin_opcode = 0x80 | opcode
        length = len(payload)
        mask_bit = 0x80
        if length <= 125:
            header = struct.pack("!BB", fin_opcode, mask_bit | length)
        elif length <= 65535:
            header = struct.pack("!BBH", fin_opcode, mask_bit | 126, length)
        else:
            header = struct.pack("!BBQ", fin_opcode, mask_bit | 127, length)
        self.sock.sendall(header + b"\x00\x00\x00\x00" + payload)

    def _recv_frame(self):
        data = self.leftover
        while len(data) < 2: data += self.sock.recv(4096)
        b1, b2 = data[0], data[1]
        opcode = b1 & 0x0F
        masked = (b2 & 0x80) != 0
        length = b2 & 0x7F
        idx = 2
        if length == 126:
            while len(data) < idx+2: data += self.sock.recv(4096)
            length = struct.unpack("!H", data[idx:idx+2])[0]; idx += 2
        elif length == 127:
            while len(data) < idx+8: data += self.sock.recv(4096)
            length = struct.unpack("!Q", data[idx:idx+8])[0]; idx += 8
        if masked:
            while len(data) < idx+4: data += self.sock.recv(4096)
            mask = data[idx:idx+4]; idx += 4
        while len(data) < idx+length: data += self.sock.recv(65536)
        payload = data[idx:idx+length]
        if masked:
            payload = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.leftover = data[idx+length:]
        return opcode, payload

    def call(self, method, params=None):
        self._id += 1
        msg_id = self._id
        msg = json.dumps({"id": msg_id, "method": method, "params": params or {}}).encode()
        self._send_frame(msg)
        while True:
            opcode, payload = self._recv_frame()
            if opcode == 0x1:
                obj = json.loads(payload.decode())
                if obj.get("id") == msg_id:
                    return obj
                # ignore events without matching id

    def eval(self, expr, return_by_value=True):
        resp = self.call("Runtime.evaluate", {"expression": expr, "returnByValue": return_by_value, "awaitPromise": True})
        result = resp.get("result", {}).get("result", {})
        if "value" in result:
            return result["value"]
        return result
