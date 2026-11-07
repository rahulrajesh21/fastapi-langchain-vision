from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()
from api.v1.chat import router




app = FastAPI()
app.include_router(
    router=router,
    prefix='/api/v1'
)
app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"]
)


