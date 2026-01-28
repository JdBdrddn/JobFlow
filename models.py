from sqlalchemy import Column, Integer, String, Date
from database import Base


class JobApplication(Base):
    __tablename__ = 'job_applications'

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    position = Column(String)
    status = Column(String)
    applied_date = Column(Date)