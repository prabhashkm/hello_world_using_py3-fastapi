'''Demo web app using python and fastapi'''

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

#def help_function():
#    '''Demo web app using python and fastapi'''
#    return None
#
#print("using help:")
#print(help_function())

app=FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query: Optional[str] = None):
    return {"item_id": item_id, "query": query}
    

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
    
