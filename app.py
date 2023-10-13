from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == "/display":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = self.server.message if hasattr(self.server, 'message') else ""
            response = f"""<!DOCTYPE html>
<html>
<head>
    <title>Message Display</title>
</head>
<body>
    <h1>Enter a message:</h1>
    <form action="/display" method="post">
        <input type="text" name="message">
        <input type="submit" value="Send">
    </form>
    
    <h2>Message Display:</h2>
    <p>{message}</p>
</body>
</html>"""
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        message = parse_qs(post_data)['message'][0]
        self.server.message = message
        self.send_response(303)
        self.send_header('Location', '/display')
        self.end_headers()
        
        # Print the message to the console
        print(f"Received message: {message}")

def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server is running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
