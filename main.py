import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional , List
from fastapi import FastAPI , Depends
from pydantic import BaseModel
import models , schemas
from database import  engine, get_db
from sqlalchemy.orm import  Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/data", response_model=List[schemas.Data] )
def test_post(db: Session = Depends(get_db)):
    #post = db.query(models.Data).all()
    post = db.query(models.Data).order_by(models.Data.id.desc()).all()
    return post

@app.get("/data/last" , response_model=schemas.Data )
def test_post(db: Session = Depends(get_db)):
    post = db.query(models.Data).order_by(models.Data.id.desc()).first()
    #post = db.query(models.Data).first()
    return post