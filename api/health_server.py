"""Temporary health endpoint for the Phase 1 API/UI container scaffold."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys


class HealthHandler(BaseHTTPRequestHandler):
    """Expose only a health check until the FastAPI app arrives in Phase 4."""

    def do_GET(self) -> None:  # noqa: N802 - matches BaseHTTPRequestHandler API
        if self.path != "/health":
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status":"phase-1-scaffold"}')

    def log_message(self, format: str, *args: object) -> None:
        """Avoid logging untrusted request contents to stdout."""
        return


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", int(sys.argv[1])), HealthHandler).serve_forever()
