from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="Core Agent", version="0.2.0")

CORE_API_KEY = os.getenv("CORE_API_KEY")

class Task(BaseModel):
    action: str
    payload: dict | None = None

@app.get("/health")
def health():
    return {"status": "alive", "role": "core-agent"}

@app.post("/execute")
def execute(
    task: Task,
    x_api_key: str = Header(None)
):
    if CORE_API_KEY and x_api_key != CORE_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "received": task.action,
        "payload": task.payload,
        "decision": "ACK - Core secured and received the task"
    }
