from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import SUDENT, TEACHER, BOOK

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/STUDENT/{id}")
async def read_student(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        student = session.get(student, id)
        return {"message": student}
    
    

@app.post("/STUDENT")
async def add_student(student: add_student):
    with Session(engine) as session:
        session.add(student)
        session.commit()
        session.refresh(student)

        return {"message": 'student'}
    
    

@app.get("/TEACHER/{id}")
async def read_teacher(id: int):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        teacher = session.get(TEACHER, id)
        return {"message": teacher}
    

@app.post("/TEACHER")
async def add_teacher(teacher: TEACHER):
    with Session(engine) as session:
        session.add(teacher)
        session.commit()
        session.refresh(teacher)
    

        return {"message": 'teacher'}


@app.get("/BOOK/{id}")
async def read_book(id: int):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        book = session.get(BOOK , id)
        return {"message": book}
    
    

@app.post("/BOOK")
async def add_book(book: BOOK):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)

        return {"message": 'book'}
