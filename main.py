# from fastapi import FastAPI
# # app=FastAPI()
# # # @app.get("/")
# # # def home():
# # #     return {'message':'you are now in venv'}

# # # @app.get("/about")
# # # def about():
# # #     return {"mes":"this is about page"}

# # # @app.get("/users/{user_id}")
# # # def get_users(user_id:int):
# # #     return {'user_id':user_id
# # #     }
# # @app.get('/user')
# # def get_user(name):
# #     return {'nmae':name}
# # @app.get("/products")
# # def get_user(limit: int=10):
# #     return {'limit':limit}

# # @app.get("/items")
# # def get_user(name:str=None, price:int=0):
# #     return {
# #         'name':name,
# #         'price':price
# #     }
# from pydantic import BaseModel
# app= FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
# @app.post("/create-user")
# def create_user(user:User):
#     return {
#         "message":'User Created',
#         'data':user
#     }

from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str
@app.post('/create_user')
def create_user(user:User):
    return{
        'msg':"user creatrd",
        'data':user
    }
class Address(BaseModel):
    city:str
    pincode:int
class User(BaseModel):
    name:str
    age:int
    address:Address
    
@app.post('/create_user')
def create_user(user:User):
    return user