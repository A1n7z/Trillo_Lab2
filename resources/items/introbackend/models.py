from sqlmodel import Field , SQLModel

class OnlineGameSurvey(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    Game_Name = str
    Genre = str
    Price = int
    Frequency = int
    Platforms = str
    Motivates = str
    Perceived_Impact = str
    Trouble = str
    Improvement = str
    Rate = str

    
    
    
    



    