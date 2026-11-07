from fastapi import APIRouter,Form
from model.request import Request
from typing import Annotated
from service.analysis import analysis
from agent.graph import checkpoint

router = APIRouter()

@router.post('/chat')
async def chat(data:Annotated[Request,Form()]):
    return await analysis(data)

@router.delete('/chat')
async def chat(thread_id:str = "default"):
    await checkpoint.adelete_thread(thread_id)
    return {"message": "Chat history deleted successfully"}

