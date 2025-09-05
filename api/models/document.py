from pydantic import BaseModel

class DocumentRequest(BaseModel):
    text: str

class SimplifiedResponse(BaseModel):
    simplified_text: str
