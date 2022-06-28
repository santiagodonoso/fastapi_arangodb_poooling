from fastapi import APIRouter
from fastapi.responses import JSONResponse
import httpx
import json
import x
import re

# PHONE_REG_EX = "^[0-9]+$"
# # test = re.search(PHONE_REG_EX, "a1234")
# test = re.match(PHONE_REG_EX, "1234")
# print(test)

from x import validate_from_to

router = APIRouter()

@router.get("/users")
async def get_users(start: str = 0, limit: int=10 ):

  # start, limit = x.validate_from_to(start, limit)
  # if start is False: return {"info":"error"}
  # return start

  """
  async with httpx.AsyncClient() as client:
    try:
      q = {"query":"FOR user IN users RETURN user"}
      res = await client.post("http://localhost:8529/_api/cursor", data=json.dumps(q))  
      print(res.content)
      res = json.loads(res.content)
      # print(res.content)
      return res["result"]
    except Exception as ex:
      return JSONResponse(status_code=500, content={"info": "upsss..."})
  """

"""
# Error on URL or Query goes to the exception
{
  "info": "upsss..."
}
"""


"""
# No users found
[]
"""

"""
# Success
[
  {
    "_key": "155",
    "_id": "users/155",
    "_rev": "_eV-6ojC---",
    "name": "Name A"
  },
  {
    "_key": "167",
    "_id": "users/167",
    "_rev": "_eV-6zwa---",
    "name": "Name B"
  }
]
"""

