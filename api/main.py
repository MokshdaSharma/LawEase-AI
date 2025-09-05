from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import routers

# Create FastAPI app
app = FastAPI(
    title="Legal Document Simplifier API",
    description="AI-powered service to simplify legal documents into plain language with multilingual support.",
    version="1.0.0"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production (e.g., your frontend domain)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(routers.upload.router, prefix="/upload", tags=["Upload"])
app.include_router(routers.simplify.router, prefix="/simplify", tags=["Simplify"])
app.include_router(routers.assistant.router, prefix="/assistant", tags=["Assistant"])
app.include_router(routers.voice.router, prefix="/voice", tags=["Voice"])

@app.get("/")
def root():
    return {"message": "Welcome to the Legal Document Simplifier API 🚀"}
