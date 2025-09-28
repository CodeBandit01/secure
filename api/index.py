
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
from http.server import BaseHTTPRequestHandler
import json


app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)

# serve static files
app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/api")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}


# api/admin.py


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/index":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "status": "ok",
                "message": "Admin backend is running",
                "users": ["alice", "bob", "charlie"]
            }

            self.wfile.write(json.dumps(data).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")


handler = Mangum(app)
