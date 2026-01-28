from fastapi import FastAPI
from database import engine, Base
import models

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Welcome to JobFlow!'}

@app.get('/test')
def test():
    return {'message': 'Your API is working!', 'database': 'connected'}