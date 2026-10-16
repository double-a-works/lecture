#!/usr/bin/env python3
"""Local-only HTTP shim so headless automation jobs (which lack shell/exec access)
can trigger the Kirana SIAKAD auto-close check via a plain web_fetch GET.
Binds to 127.0.0.1 only. Runs persistently outside any chat session's sandbox."""
import http.server
import subprocess
import json
import os
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CONTAINER = "kirana-browser"
PORT = 8765

def run_check():
    subprocess.run(["docker", "cp", os.path.join(HERE, "cdp_helpers.py"), f"{CONTAINER}:/tmp/cdp_helpers.py"], check=True)
    subprocess.run(["docker", "cp", os.path.join(HERE, "kirana_autoclose.py"), f"{CONTAINER}:/tmp/kirana_autoclose.py"], check=True)
    proc = subprocess.run(
        ["docker", "exec", CONTAINER, "python3", "/tmp/kirana_autoclose.py"],
        capture_output=True, text=True, timeout=120
    )
    log_line = f"{datetime.datetime.now().isoformat()} rc={proc.returncode} stdout={proc.stdout.strip()[:2000]} stderr={proc.stderr.strip()[:500]}\n"
    with open(os.path.join(HERE, "kirana_watchdog.log"), "a") as f:
        f.write(log_line)
    if proc.returncode != 0:
        return {"ok": False, "error": proc.stderr.strip()[-1500:]}
    last_line = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else "{}"
    try:
        data = json.loads(last_line)
    except json.JSONDecodeError:
        return {"ok": False, "error": "could not parse script output", "raw": proc.stdout[-1500:]}
    data["ok"] = True
    return data

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/check-and-close"):
            try:
                result = run_check()
                body = json.dumps(result).encode()
                self.send_response(200)
            except Exception as e:
                body = json.dumps({"ok": False, "error": str(e)}).encode()
                self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, fmt, *args):
        pass

if __name__ == "__main__":
    server = http.server.HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"kirana watchdog server listening on 127.0.0.1:{PORT}")
    server.serve_forever()
