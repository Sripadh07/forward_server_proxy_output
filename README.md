# forward_server_proxy_output
# Working 
##  1. Run the code forward_proxy_server.py it listens to specified port
##  2. And when we enter the 'localhost:8000' in our web browser  it will redirect to requested website url either the case of 'http or https'.
## Description about proxy server
- ProxyServer acts as mediater between client and server so it is nothing but it forwards the request of clients in such a way that it doesnt show client identity to requested server.instead it displays anoother identity which is nothing but ip address ,now we can say that it is making secure path for client to request to the server.
# Functionality
- At first I assigned a url to proxy as example.com any url can be assigned in the TARGET_HOST variable of the code
- And then as per objective it should display accepted information and response whether it is http or https
- The libraries used are BaseHTTPRequestHandler it handles  http requests , ThreadingHTTPServer library helps in accepting multiple requests concurrently.
- For HTTPS using ssl library it is encrypted as https provides security.
- In proxy handler function the http and https requests are handled in which they redirects to their respective functions to redirect the proxy for the requested url
- For accessing multiple requests concurrently in run_proxy_server function i used ThreadingHTTPServer library to create multiple requests so for that  'httpd.serve_forever()' this command helps in doing that
- And to handle https requests i used ssl.wrap_socket method in library of ssl to certify server certificate and private key and they are generated in the main function.
- In this way the code accepts request and generate and response as per the objective.
