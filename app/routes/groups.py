from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Group

router = APIRouter()

@router.get("/")
def get_groups(db: Session = Depends(get_db), page: int = 1, sort_by: str = "name", order: str = "asc"):
    query = db.query(Group)
    if order == "desc":
        query = query.order_by(getattr(Group, sort_by).desc())
    else:
        query = query.order_by(getattr(Group, sort_by).asc())
    
    groups = query.offset((page - 1) * 10).limit(10).all()
    return groups

