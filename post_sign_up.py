from fastapi import APIRouter
from fastapi.responses import JSONResponse
import httpx
import json

router = APIRouter()

@router.post("/sign-up")
async def sign_up():
  async with httpx.AsyncClient() as client:
    try:
      user = {"name":"Name X"}
      q = {
            "query":"INSERT @user IN users RETURN NEW", 
            "bindVars":{
              "user": user
            }
          }
      res = await client.post("http://localhost:8529/_api/cursor", data=json.dumps(q))
      print(res.content)
      # Convert string res into an object
      res = json.loads(res.content)
      if res["error"]: 
        return JSONResponse(status_code=500, content={"info":res["errorMessage"]})
      return {"info":"user created", "user_key":res["result"][0]["_key"]}
    except Exception as ex:
      print(ex)
      return JSONResponse(status_code=500, content={"info":"upsss..."})


"""
# Query error
{"code":400,
"error":true,
"errorMessage":"AQL: syntax error, unexpected identifier near \'INx users\' at position 1:14 (while parsing)",
"errorNum":1501}
"""

"""
# res.content
{"result":[],"hasMore":false,"cached":false,
"extra":{"warnings":[],
"stats":{"writesExecuted":1,"writesIgnored":0,"scannedFull":0,"scannedIndex":0,"filtered":0,"httpRequests":0,"executionTime":3.0590000005759066e-4,"peakMemoryUsage":0}},
"error":false,"code":201}
"""

"""
{"result":[{"_key":"3515","_id":"users/3515","_rev":"_eVAtwnS---","name":"Name X"}],
"hasMore":false,"cached":false,"extra":{"warnings":[],
"stats":{"writesExecuted":1,"writesIgnored":0,"scannedFull":0,"scannedIndex":0,"filtered":0,"httpRequests":0,"executionTime":3.9170000036392594e-4,"peakMemoryUsage":0}},
"error":false,"code":201}
"""