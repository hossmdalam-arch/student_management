from model.Student_model import Students_model
from database import session_lock

class StudentRepisitory:
    def __init__(self):
        self.connection=session_lock()
    def get_all(self):
        return self.connection.query(Students_model).all()
    def add_student(self,playload:Students_model):
        self.connection.add(playload)
        self.connection.commit()