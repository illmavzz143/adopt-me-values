from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import urllib.error
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Sprawdzamy, o jaki adres pyta skrypt z gry
        if self.path.startswith("/value"):
            # Przykład pobierania danych (możesz tu podmienić docelowy adres URL, który chcesz scrapować/obsługiwać)
            target_url = "https://jsonplaceholder.typicode.com/todos/1" # Przykładowy testowy URL
            
            try:
                req = urllib.request.Request(
                    target_url, 
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                with urllib.request.urlopen(req) as response:
                    data = response.read().decode('utf-8')
                    
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data.encode('utf-8'))
                
            except urllib.error.URLError as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=10000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serwer dziala na porcie {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
