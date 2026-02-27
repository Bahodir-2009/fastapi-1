from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int

@app.get('/')
def home():
    """Bu sahifa"""
    return {
        'xabar':f'Salom Fastapi'
    }

@app.get('/hello/{name}')
def hello(name:str):
    """Bu sahifada userlarga salom berdi."""
    return {
        'xabar':f'Salom {name}'
    }

@app.post('/users')
def user_add(user:User):
    """Bu user data sini saqlaydi"""
    return{
        'xabar':'User data saqlaydi.',
        'data':user
    }
