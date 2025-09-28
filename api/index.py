
# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from mangum import Mangum
# from http.server import BaseHTTPRequestHandler
# import json


# app = FastAPI(
#     title="Vercel + FastAPI",
#     description="Vercel + FastAPI",
#     version="1.0.0",
# )

# # serve static files
# app.mount("/public", StaticFiles(directory="public"), name="public")

# @app.get("/api")
# def read_root():
#     return {"message": "Hello from FastAPI on Vercel!"}


# # api/admin.py


# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == "/api/index":
#             self.send_response(200)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()

#             data = {
#                 "status": "ok",
#                 "message": "Admin backend is running",
#                 "users": ["alice", "bob", "charlie"]
#             }

#             self.wfile.write(json.dumps(data).encode("utf-8"))
#         else:
#             self.send_response(404)
#             self.end_headers()
#             self.wfile.write(b"Not found")


# handler = Mangum(app)

# api/index.py
# from http.server import BaseHTTPRequestHandler
# import json

# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         # Only respond to /api
#         if self.path == "/api" or self.path == "/api/":
#             self.send_response(200)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()

#             data = {
#                 "status": "ok",
#                 "message": "Python backend is running on Vercel!",
#                 "users": ["alice", "bob", "charlie"]
#             }

#             self.wfile.write(json.dumps(data).encode("utf-8"))
#         else:
#             self.send_response(404)
#             self.end_headers()
#             self.wfile.write(b"Not found")

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/admin-data")
def get_admin_data():
    # In the future, this can come from Supabase
    data = {
        "message": "Admin API is working!",
        "users": ["alice@example.com", "bob@example.com", "charlie@example.com"]
    }
    return JSONResponse(content=data)
