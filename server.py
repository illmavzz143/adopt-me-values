from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        # Testowa odpowiedź, zaraz ją rozbudujemy o scraper
        data = {"status": "online", "message": "Serwer proxy dla Robloxa działa!"}
        self.wfile.write(json.dumps(data).encode("utf-8"))

def run():
    server_address = ('', 10000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Serwer ruszył na porcie 10000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
