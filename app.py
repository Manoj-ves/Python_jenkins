from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello from Python HTTP server!')


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server started on port {port}')

    # Schedule a task to stop the server after 10 seconds
    def stop_server():
        print("Shutting down server...")
        httpd.shutdown()

    # Start the server
    httpd_thread = threading.Thread(target=httpd.serve_forever)
    httpd_thread.start()

    # Sleep for 10 seconds
    time.sleep(10)

    # Stop the server after 10 seconds
    stop_server()
    httpd_thread.join()


if __name__ == "__main__":
    run()
