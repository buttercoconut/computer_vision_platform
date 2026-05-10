# app/models/label.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=False)
    category = Column(String, nullable=False)
    confidence = Column(String, nullable=True)

    image = relationship("Image", backref="labels")

    def __repr__(self):
        return f"<Label id={self.id} category={self.category} confidence={self.confidence}>"
