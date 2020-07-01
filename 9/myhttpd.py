from http.server import BaseHTTPRequestHandler,HTTPServer

class MyHander(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:],'r')
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404,'File Not Found:{}'.format(self.path))
def main():
    try:
        server = HTTPServer(('',80),MyHander)
        print('Welcome')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shutting dowm...')
        server.socket.close()

if __name__ == '__main__':
    main()