from fastapi import FastAPI
from router import student_control

from database import base,enginee
from utils.schema import Student_creat_schema, Student_respons_schema

base.metadata.create_all(bind=enginee)

app=FastAPI(title="sorita")
app.include_router(student_control.router)