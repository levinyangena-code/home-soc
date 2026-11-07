"""Small temporary HTTP health endpoint used by the Phase 1 service scaffold."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys


class HealthHandler(BaseHTTPRequestHandler):
    """Return a minimal status response without exposing files or request data."""

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
