from sqlmodel import Session , select

from database import create_db_and_tables, engine
from models import GPUGamingSurvey



def main():
    create_db_and_tables()


    
    survey1 = Game_Name(='Dota', Genre='MOBA', Price=Free2play, Frequency=3, Platform='PC', Motivates='For Fun', Perceive_Impact='Patience', Trouble='None so Far', Improvement='Add more modes', Rate='10/10')
    survey2 = Game_Name(='S4 League', Genre='MMO', Price=Free2play, Frequency=2, Platform='PC', Motivates='For Fun & Meet foreign friends', Perceive_Impact='Learn other language', Trouble='None so Far', Improvement='None so far', Rate='10/10')
    survey3 = Game_Name(='PUBG', Genre='Battle Royal', Price=Free2play, Frequency=1, Platform='CP', Motivates='For Fun', Perceive_Impact='Reflexes', Trouble='None so Far', Improvement='Add more modes', Rate='10/10')

    with Session(engine) as session:
        session.add(survey1)
        session.add(survey2)
        session.add(survey3)
        session.commit()


if __name__ == "__main__":
    main()from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware

from models import OnlineGameSurvey

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/gpugamingsurvey/{id}")
async def read_survey(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        gpugamingsurvey = session.get(OnlineGameSurvey, id)
        return {"message": OnlineGameSurvey}
    

@app.post("/GPUGamingSurvey")
async def root(GPUGamingSurvey  : GPUGamingSurvey):
    with Session(engine) as session:
        session.add(OnlineGameSurvey)
        session.commit()
        session.refresh(OnlineGameSurvey)
        return {"message": OnlineGameSurvey}body{

