from service.student_Service import StudentService
from fastapi import APIRouter,status
from utils.schema import Student_respons_schema,Student_creat_schema

router=APIRouter(prefix="/students",tags=["Students"])

@router.get("/all", status_code=status.HTTP_200_OK)
def get_student_all_contrl():
    service=StudentService()
    return service.get_student_service() 

@router.post("/all", status_code=status.HTTP_201_CREATED)
def add_student_all_contrl(playload:Student_creat_schema):
    service=StudentService()
    service.all_student_service(playload)