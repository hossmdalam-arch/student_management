from repository.repository import StudentRepisitory
from utils.schema import Student_creat_schema,Student_respons_schema
from model.Student_model import Students_model


class StudentService:
    def __init__(self):
        self.repositor=StudentRepisitory
    def get_all_service(self):
        student_list=[]
        students=self.repositor.get_all()

        for student in students:
            student_list.append(Student_respons_schema.model_validate(student))
        return student_list
    
    def add_all_service(self,studentplayload:Student_creat_schema):
        student=Students_model(**studentplayload.dict)
        self.repositor.add_student(student)