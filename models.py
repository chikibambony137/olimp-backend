from sqlalchemy import Column, BIGINT, VARCHAR
from database import Base

class AboutMe(Base):
    __tablename__ = 'aboutme'
    id = Column(BIGINT, primary_key=True, index=True)

    text = Column(VARCHAR)
