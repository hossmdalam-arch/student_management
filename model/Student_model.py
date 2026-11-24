from database import base
from sqlalchemy import Column,String,INTEGER

class Students_model(base):
    __tablename__="Students"
    id=Column(INTEGER,autoincrement=True,index=True,primary_key=True)
    name=Column(String(100))
    department=Column(String(100))
    age=Column(INTEGER)
    mark=Column(INTEGER)