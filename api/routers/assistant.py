from fastapi import APIRouter
from models.assistant import AssistantQuery, AssistantResponse
from services.assistant_agent import run_assistant

router = APIRouter()

@router.post("/", response_model=AssistantResponse)
async def ask_assistant(query: AssistantQuery):
    answer = run_assistant(query.query, lang=query.lang)
    return {"answer": answer}
