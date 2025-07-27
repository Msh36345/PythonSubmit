from fastapi import FastAPI
from Manager import Manager
from fastapi.responses import HTMLResponse
# import uvicorn


dic = {"Pclass": 3,  "Sex": "male", "Age": 22, "SibSp": 0, "Parch": 0, "Fare": 7.25, "Embarked": "S"}
manager = Manager(dic)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return manager.run()

# if __name__ == "__main__":
    # uvicorn.run(app,host="127.0.0.1",port=8090)