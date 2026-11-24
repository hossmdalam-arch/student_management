from pydantic import BaseModel,Field

class Student_creat_schema(BaseModel):
    name:str
    department:str
    age:int= Field(le=40,ge=16)
    mark:int

class Student_respons_schema(Student_creat_schema):
    id:int

    class Config:
        from_attributes=True