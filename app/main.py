from fastapi import FastAPI,Response,HTTPException,status,Depends,APIRouter
from .database import engine,SessionLocal,get_db
from . import models
from .routers import post,user,auth,vote,joins
from .config import settings
from fastapi.middleware.cors import CORSMiddleware



origins = ["*"]

app = FastAPI()
#Add middleware
app.add_middleware(CORSMiddleware,allow_origins=origins,
                   allow_credentials=True,allow_methods=["*"],
                   allow_headers=["*"],)

 
"""
while True:
    try:
        conn = psycopg2.connect(host='localhost',database='fastAPI',user = 'postgres',password = 'j0th3s1s!',cursor_factory= RealDictCursor)
        cursor = conn.cursor()
        print("Connection successfull")
        break
    except Exception as error:
        print("Connection failed!")
        print("Error :",error)
        time.sleep(2)
 """


if app == True:
   print("connected!")

models.Base.metadata.create_all(bind=engine)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(joins.router)

@app.get("/")
def root():
    return "Welcome to my api"
