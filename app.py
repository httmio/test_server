from fastapi import FastAPI, Request
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
    return qrcode
