from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, nullable=False)
    data = Column(String, nullable=False)
    time = Column(String, nullable=False)