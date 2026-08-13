from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.auth.dependencies import CurrentUser,get_current_user
import uvicorn

from app.config import settings

app = FastAPI(title="Document Copilot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health() -> dict[str,str]:
    return {"status": "ok"}

@app.get("/me")
async def get_me(
    user: CurrentUser = Depends(get_current_user)
    ):
    return user

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)