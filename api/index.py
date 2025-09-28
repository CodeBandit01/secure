# from fastapi import FastAPI
# from mangum import Mangum

# app = FastAPI()


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from mangum import Mangum

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

handler = Mangum(app)
