from pydantic import BaseModel

class AssistantQuery(BaseModel):
    query: str
    lang: str | None = None

class AssistantResponse(BaseModel):
    answer: str
