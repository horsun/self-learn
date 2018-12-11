from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class TodoHandle(BaseHTTPRequestHandler):
    TODOS = []

    def do_GET(self):
        if self.path != '/':
            self.send_error(404, 'page not found')
            return
        message = json.dumps(self.TODOS)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(message))


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8888), TodoHandle)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()
