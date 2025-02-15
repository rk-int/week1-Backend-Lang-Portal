from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import WordReviewItem
from app.schemas import ReviewCreate

router = APIRouter()

@router.post("/{session_id}/review")
def create_review(session_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    new_review = WordReviewItem(word_id=review.word_id, study_session_id=session_id, correct=review.correct)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

