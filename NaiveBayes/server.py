import uvicorn
from fastapi import FastAPI,Request
from main import Manager

app=FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "hello world"}

# @app.get("/{name}")
# async def root(name):
#     return {"enter name": name}

@app.get("/dict")
async def predict(request: Request):
    input_dict = dict(request.query_params)
    result = manager.sel.check_dict(input_dict)
    return {"result": result}

path = '/Users/mosheshulman/PycharmProjects/Data/PythonProjectsSubmi/NaiveBayes/csv/buys computer.csv'
manager=Manager(path,False)


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8080)