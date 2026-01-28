from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()


password = os.getenv('DATABASE_PASSWORD')


DATABASE_URL = f'postgresql://postgres:{password}@localhost/jobflow_db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()