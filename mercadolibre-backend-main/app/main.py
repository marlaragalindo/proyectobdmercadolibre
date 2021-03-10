from fastapi import FastAPI
from app.api.router import api_router
from starlette.middleware.cors import CORSMiddleware

from app.db.base import init_db

app = FastAPI()
app.include_router(api_router)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])


@app.on_event("startup")
async def startup_event():
    init_db(app)
