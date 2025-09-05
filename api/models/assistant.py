from pydantic import BaseModel

class AssistantRequest(BaseModel):
    query: str
    lang: str | None = None

class AssistantResponse(BaseModel):
    answer: str
