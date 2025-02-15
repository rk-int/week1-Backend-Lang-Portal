from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Word

router = APIRouter()

@router.get("/")
def get_words(db: Session = Depends(get_db), page: int = 1, sort_by: str = "kanji", order: str = "asc"):
    query = db.query(Word)
    if order == "desc":
        query = query.order_by(getattr(Word, sort_by).desc())
    else:
        query = query.order_by(getattr(Word, sort_by).asc())
    
    words = query.offset((page - 1) * 10).limit(10).all()
    return words

