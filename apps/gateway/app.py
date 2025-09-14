from fastapi import FastAPI
from pydantic import BaseModel
import os, json

app = FastAPI()

class Control(BaseModel):
    action: str  # "start" | "stop" | "reset"

STATE = {"running": False}

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/sim")
def control(ctrl: Control):
    if ctrl.action == "start": STATE["running"] = True
    if ctrl.action == "stop":  STATE["running"] = False
    if ctrl.action == "reset": STATE.update({"running": False})
    return STATE

@app.get("/state")
def state():
    # in real build, read from Redis/stream; placeholder:
    try:
        with open("/artifacts/runs/latest.json") as f: return json.load(f)
    except Exception: return {"running": STATE["running"], "tick": 0}
