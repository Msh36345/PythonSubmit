import uvicorn
from fastapi import FastAPI

app=FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "hello world"}

@app.get("/{name}")
async def root(name):
    return {"enter name": name}

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8080)