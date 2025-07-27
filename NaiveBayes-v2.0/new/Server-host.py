from fastapi import FastAPI
from Manager import Manager
# import uvicorn

path = "titanic.csv"
manager = Manager(path)

app = FastAPI()

@app.get("/")
async def root():
    return manager.run_host()

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=8080)