import json
from http.server import BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from http.server import HTTPServer

from ai_code_engine.engine import process_file


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class Handler(BaseHTTPRequestHandler):

    def do_POST(self):

        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)

        try:
            data = json.loads(body)

            code = data.get("code")
            path = data.get("path", "file.py")

            if not code:
                raise Exception("No code provided")

            result = process_file(code, path)

        except Exception as e:
            result = {
                "error": str(e)
            }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(result).encode())


def run_server():

    server = ThreadedHTTPServer(("localhost", 5050), Handler)

    print("AI CODE ENGINE SERVER RUNNING ON 5050")

    server.serve_forever()