import http.server
import ssl

httpd = http.server.HTTPServer(('localhost', 1337), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./SSL_keys/localhost.pem', keyfile='./SSL_keys/localhost-key.pem', server_side=True)
httpd.serve_forever()