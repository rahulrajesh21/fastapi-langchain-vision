from pydantic import BaseModel
from fastapi import UploadFile
from typing import Optional


class Request(BaseModel):
    prompt:str
    image: Optional[UploadFile] = None
    thread_id:Optional[str] = "default"



