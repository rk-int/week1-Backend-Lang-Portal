from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import StudySession
from app.schemas import StudySessionCreate

router = APIRouter()

@router.post("/")
def create_study_session(session: StudySessionCreate, db: Session = Depends(get_db)):
    new_session = StudySession(group_id=session.group_id, study_activity_id=session.study_activity_id)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

