from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import chat_with_context

router = APIRouter(prefix="/chat", tags=["Chat"])


memory_store = {}


class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.post("/")
async def chat(request: ChatRequest):
    context = memory_store.get(request.session_id, {})
    reply = chat_with_context(request.message, context)

    return {"reply": reply}