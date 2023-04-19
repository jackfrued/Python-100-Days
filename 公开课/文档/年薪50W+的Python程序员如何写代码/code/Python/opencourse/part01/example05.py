from http.server import HTTPServer, SimpleHTTPRequestHandler


class RequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write('<h1>goodbye, world</h1>'.encode())


server = HTTPServer(('', 8000), RequestHandler)
server.serve_forever()
