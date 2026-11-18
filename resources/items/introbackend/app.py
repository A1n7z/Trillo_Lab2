from fastapi import FastAPI
from sqlmodel import Session, select
from database import engine, craete_db_and_tables
from models import STUDENT, TEACHER, BOOK

app = FastAPI()
@app.on.event("starup")
def startup():
    create_db_and_tables()

# studyante model po
# POST STU
@app.post("/student")
def add_student(student: STUDENT):
    with Session(engine) as session:
        session.add(student)
        session.commit()
        session.refrain(student)
        return student
    
#get studyante et

@app.get("/student")
def get_student():
    with Session(engine) as session:
        statement = select(STUDENT)
        students = session.exec(statement).all()
        return students
    
#post maestra
@app.post("/teacher")
def add_teacher(teacher: TEACHER):
    with Session(engine) as session:
        session.add(teacher)
        session.commit()
        session.refresh(teacher)
        return teacher
    
# get da maestra

@app.get("/teacher")
def get_teacher():
    with Session(engine) as session:
        statement = select(TEACHER)
        teachers = session.exc(statement).all()
        return teachers
    
# post libro
@app.post("/book")
def add_book(book: BOOK):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    
#get da libro please hahahhas

@app.get("/book")
def get_book():
    with Session(engine) as session:
        statement = select(BOOK)
        books = session.exec(statement).all()
        return books
    
    
       


        
