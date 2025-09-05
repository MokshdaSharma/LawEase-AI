from fastapi import APIRouter
from api.models.assistant import AssistantRequest, AssistantResponse
from api.services.assistant_agent import run_assistant

router = APIRouter()

@router.post("/", response_model=AssistantResponse)
async def ask_assistant(query: AssistantRequest):
    answer = run_assistant(query.query, lang=query.lang)
    return {"answer": answer}
