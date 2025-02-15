from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, JSON, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.database import Base

class Word(Base):
    __tablename__ = "words"
    
    id = Column(Integer, primary_key=True, index=True)
    kanji = Column(String, nullable=False)
    romaji = Column(String, nullable=False)
    english = Column(String, nullable=False)
    parts = Column(JSON, nullable=False)
    
    groups = relationship("WordGroup", back_populates="word")
    
class Group(Base):
    __tablename__ = "groups"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    words_count = Column(Integer, default=0)
    
    words = relationship("WordGroup", back_populates="group")
    
class WordGroup(Base):
    __tablename__ = "word_groups"
    
    word_id = Column(Integer, ForeignKey("words.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)
    
    word = relationship("Word", back_populates="groups")
    group = relationship("Group", back_populates="words")
    
class StudyActivity(Base):
    __tablename__ = "study_activities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    
class StudySession(Base):
    __tablename__ = "study_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    study_activity_id = Column(Integer, ForeignKey("study_activities.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    group = relationship("Group")
    study_activity = relationship("StudyActivity")
    reviews = relationship("WordReviewItem", back_populates="study_session")
    
class WordReviewItem(Base):
    __tablename__ = "word_review_items"
    
    id = Column(Integer, primary_key=True, index=True)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False)
    study_session_id = Column(Integer, ForeignKey("study_sessions.id"), nullable=False)
    correct = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    word = relationship("Word")
    study_session = relationship("StudySession", back_populates="reviews")

