from fastapi import APIRouter
from models.document import DocumentRequest, SimplifiedResponse
from services.simplifier import simplify_text

router = APIRouter()

@router.post("/", response_model=SimplifiedResponse)
async def simplify_document(doc: DocumentRequest):
    simplified = simplify_text(doc.text)
    return {"simplified_text": simplified}
