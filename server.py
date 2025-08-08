import os
from http.server import SimpleHTTPRequestHandler, HTTPServer


def run():
    port = int(os.environ.get("PORT", 5000))
    handler = SimpleHTTPRequestHandler
    with HTTPServer(("", port), handler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()


if __name__ == "__main__":
    run()
