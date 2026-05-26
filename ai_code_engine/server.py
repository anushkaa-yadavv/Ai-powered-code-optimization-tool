from fastapi import FastAPI
from pydantic import BaseModel

from ai_code_engine.engine import process_file

app = FastAPI()


class CodeInput(BaseModel):
    code: str
    path: str


@app.post("/analyze")
def analyze(data: CodeInput):

    return process_file(data.code, data.path)