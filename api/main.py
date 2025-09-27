from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

handler = Mangum(app)