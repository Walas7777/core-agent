from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Core Agent", version="0.1.0")

class Task(BaseModel):
    action: str
    payload: dict | None = None

@app.get("/health")
def health():
    return {"status": "alive", "role": "core-agent"}

@app.post("/execute")
def execute(task: Task):
    return {
        "received": task.action,
        "payload": task.payload,
        "decision": "ACK - Core received the task"
    }
