from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import mysql_create_session

class Register_User(BaseModel):
  user_email:str
  user_password:str
  user_name:str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/register")
def register(user:Register_User):
  conn,cur = mysql_create_session()
  user_dict = user.model_dump()
  user_email,user_password,user_name = user_dict.values()
  try:
    sql4 = 'INSERT INTO Users(user_email, user_password, user_name) VALUES (%s, %s, %s)'
    cur.execute(sql4,(user_email, user_password, user_name))

    conn.commit()
    return {f'{user_name}'}
  except:
    raise HTTPException(status_code=404, detail="회원가입 실패")
  
  finally:
     conn.close()
     cur.close()
