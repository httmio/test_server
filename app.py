from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class QRCode(BaseModel):
    itemNo: str
    content: str


@app.get("/hello")
def hello():
    return "Hello, World!"


@app.post("/upload")
async def upload(request: Request):
    qrcode = await request.body()
    print(f"Local Server Msg : QRCode Json = {qrcode}")
    return qrcode


@app.post("/vaild_qrcode")
async def vaild_qrcode(qrcode: QRCode):
    print(f"Local Server Msg : QRCode Json = {qrcode}")
    return qrcode


@app.get("/lineme", response_class=HTMLResponse)
async def lineme_test():
    html_file = open("line_test.html", "r").read()
    return html_file
