from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def test_page():
    return {"ok": True}

@app.get("/machines")
def get_machines():
    return {"ok": True}