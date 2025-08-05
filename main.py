from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Message(BaseModel):
    id: int
    text: str

messages: List[Message] = []

@app.get("/")
def read_root():
    return {"message": "Привіт! Це простий FastAPI-сервер."}

@app.get("/messages", response_model=List[Message])
def get_messages():
    return messages

@app.post("/messages", response_model=Message)
def add_message(msg: Message):
    messages.append(msg)
    return msg