import logging
from fastapi import APIRouter

router = APIRouter(
    prefix="/summarize",
    tags = ["summarize"],
)

@router.post("/")
def summarize():
    return "Document Summarized"