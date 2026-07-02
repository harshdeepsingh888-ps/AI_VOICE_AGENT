from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.llm_service import llm_service

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    ai_response = llm_service.generate_response(
        request.session_id,
        request.message
    )

    return ChatResponse(
        response=ai_response
    )