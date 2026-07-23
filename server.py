from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Niezależnie od tego, o jaki adres pyta Delta, zawsze zwracamy dane
        data = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        }
        
        response_body = json.dumps(data).encode('utf-8')
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response_body)

def run():
    server_address = ('', 10000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Serwer ruszył...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
