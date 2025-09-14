from fastapi import FastAPI
from pydantic import BaseModel
import subprocess, tempfile, os, json

app = FastAPI()

class RunReq(BaseModel): code: str

@app.post("/tools/run_script")
def run_script(req: RunReq):
    with tempfile.TemporaryDirectory() as d:
        fp = os.path.join(d, "prog.py")
        open(fp, "w").write(req.code)
        p = subprocess.run(["python", fp], capture_output=True, text=True, timeout=5)
        return {"rc": p.returncode, "stdout": p.stdout[-2000:], "stderr": p.stderr[-2000:]}
