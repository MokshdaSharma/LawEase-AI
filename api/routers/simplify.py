from fastapi import APIRouter
from api.models.document import DocumentRequest, SimplifiedResponse
from api.services.simplifier import simplify_text

router = APIRouter()

@router.post("/", response_model=SimplifiedResponse)
async def simplify_document(doc: DocumentRequest):
    simplified = simplify_text(doc.text)
    return {"simplified_text": simplified}
