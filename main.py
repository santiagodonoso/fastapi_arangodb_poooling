from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx
import json

# docker run -e ARANGO_NO_AUTH=1 -p 8529:8529 -d --name fastapi-app-3.9.1 arangodb:3.9.1

# Check connection pool
# netstat -n | find "8529"

##############################
# Pool
# Doesn't work. Every request send creates new entry in netstat
# limits = httpx.Limits(max_keepalive_connections=2, max_connections=2)
# client = httpx.AsyncClient(limits=limits)

headers = {"Connection": "keep-alive"}

client1 = httpx.AsyncClient(headers=headers)
client2 = httpx.AsyncClient(headers=headers)
freeClients = [ client1, client2 ]

##############################
# import get_users
import post_sign_up
import get_user_by_id

##############################
app = FastAPI()

##############################
@app.get("/")
async def root():
  return {"info":"ok"}

##############################
@app.get("/users")
async def get_users():
  try:
    client = freeClients.pop(0) if len(freeClients) else httpx.AsyncClient()  
    print("1. is client closed:", client.is_closed)
    q = {"query":"FOR user IN users RETURN user"}
    res = await client.post("http://localhost:8529/_api/cursor", data=json.dumps(q))  
    freeClients.append(client)
    res = json.loads(res.content)
    print("2. is client closed:", client.is_closed)
    print("base_url", client.base_url)
    return res["result"]    
  except Exception as ex:
    print(ex)
    return {"info":"error"}

##############################
# GET     get all users
# app.include_router(get_users.router)

##############################
app.include_router(get_user_by_id.router)

##############################
# POST    sign up
app.include_router(post_sign_up.router)


