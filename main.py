from fastapi import FastAPI
import uvicorn

from mylib.logic import wiki
from mylib.logic import search_wiki

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API for search or wiki"}

@app.get("/search/{value}")
async def search(value: str):
    """search wikipedia"""

    search_result = search_wiki(value)
    return {"result": search_result}

@app.get("/wiki/{value}")
async def wiki_get(value: str):
    """get value from wiki"""

    get_wiki = wiki(value)
    return {"wiki_value": get_wiki}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
