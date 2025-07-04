from fastapi import APIRouter
from app.data.processor import generate_report

router = APIRouter()

@router.get("/report")
def get_report():
    report = generate_report()
    return {"report": report}
