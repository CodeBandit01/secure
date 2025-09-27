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

@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

# 👇 this is what Vercel needs
handler = Mangum(app)
