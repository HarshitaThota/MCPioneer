# toy MCP server exposing: search_docs(query), get_passage(doc_id, span)
from fastapi import FastAPI
from pydantic import BaseModel
import glob, json

app = FastAPI()
DOCS = {p: open(p).read() for p in glob.glob("/data/*.txt")}

class Q(BaseModel): query: str
class P(BaseModel): doc_id: str; start: int; end: int

@app.post("/tools/search_docs")
def search_docs(q: Q):
    hits=[]
    for doc_id, text in DOCS.items():
        if q.query.lower() in text.lower(): hits.append({"doc_id": doc_id, "score": 1.0})
    return {"hits": hits[:10]}

@app.post("/tools/get_passage")
def get_passage(p: P):
    return {"doc_id": p.doc_id, "passage": DOCS[p.doc_id][p.start:p.end]}
