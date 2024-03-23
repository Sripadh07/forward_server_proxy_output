from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import ssl
from urllib.parse import urlparse

TARGET_HOST = "example.com"
TARGET_URL = "http://" + TARGET_HOST
TARGET_URL = "https://" + TARGET_HOST

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)

        if not parsed_url.netloc:
            self.path = TARGET_URL + self.path

        if self.path.startswith("http://"):
            self.handle_http()
        elif self.path.startswith("https://"):
            self.handle_https()
        else:
            self.send_error(400, "Invalid URL")

    def handle_http(self):
        # Print information about the incoming request
        print("Incoming HTTP Request:", self.path)

        # Redirecting to the requested URL
        self.send_response(302)
        self.send_header('Location', self.path)
        self.end_headers()

    def handle_https(self):
        # Print information about the incoming request
        print("Incoming HTTPS Request:", self.path)

        # Redirect to the requested URL
        self.send_response(302)
        self.send_header('Location', self.path)
        self.end_headers()

def run_proxy_server(port, use_ssl=False, certfile=None, keyfile=None):
    server_address = ('', port)
    httpd = ThreadingHTTPServer(server_address, ProxyHandler)
    print('Proxy server running on port', port)
    
    if use_ssl:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=keyfile, certfile=certfile, server_side=True)
        print('Proxy server running on port', port, 'for HTTPS')
        
    httpd.serve_forever()

if __name__ == '__main__':
    HTTP_PORT = 8000  # You can change the HTTP port as needed
    HTTPS_PORT = 8443  # You can change the HTTPS port as needed
    CERTFILE = 'path/to/certificate.crt'  # Provide path to your SSL certificate file
    KEYFILE = 'path/to/private_key.key'  # Provide path to your private key file

    run_proxy_server(HTTP_PORT)

    run_proxy_server(HTTPS_PORT, use_ssl=True, certfile=CERTFILE, keyfile=KEYFILE)
