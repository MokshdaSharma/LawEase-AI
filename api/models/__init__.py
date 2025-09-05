"""
Models package initializer.
Exposes Pydantic schemas for API request/response validation.
"""

# api/models/__init__.py
from .document import DocumentRequest, SimplifiedResponse
from .assistant import AssistantRequest, AssistantResponse

__all__ = [
    "DocumentRequest",
    "SimplifiedResponse",
    "AssistantRequest",
    "AssistantResponse",
]

