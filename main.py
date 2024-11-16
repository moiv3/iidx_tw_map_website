from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/test")
def test_page():
    return {"ok": True}

@app.get("/cabinets/list")
def get_cabinet_list():
    return {"cabinet_list": ["TDJ0001","TDJ0002","TDJ0003",]}

@app.get("/cabinets/{cabinet_id}")
def get_cabinet_detail(cabinet_id: str):
    return {"cabinet_id": cabinet_id, "result": "Nothing here!"}

@app.get("/cabinets")
def get_cabinet_page():
    return FileResponse("static/cabinet.html")