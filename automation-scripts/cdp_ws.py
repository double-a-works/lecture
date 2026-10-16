import asyncio, websockets, json, urllib.request

async def get_ws_url():
    data = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json/list").read())
    for t in data:
        if t.get("type") == "page" and "portaldosen" in t.get("url", ""):
            return t["webSocketDebuggerUrl"]
    raise Exception("no portal page tab found")

class Driver:
    def __init__(self, ws):
        self.ws = ws
        self._id = 0

    async def send(self, method, params=None):
        self._id += 1
        mid = self._id
        await self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        while True:
            resp = json.loads(await self.ws.recv())
            if resp.get("id") == mid:
                return resp

    async def eval(self, expr):
        r = await self.send("Runtime.evaluate", {"expression": expr, "returnByValue": True, "awaitPromise": True})
        res = r.get("result", {}).get("result", {})
        if "value" in res:
            return res["value"]
        return res

async def connect():
    ws_url = await get_ws_url()
    ws = await websockets.connect(ws_url, max_size=50 * 1024 * 1024)
    d = Driver(ws)
    await d.send("Runtime.enable")
    await d.send("DOM.enable")
    return d
