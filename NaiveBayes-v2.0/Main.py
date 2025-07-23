from Manager import Manager


path = "titanic.csv"

dic = {"Pclass": 3,  "Sex": "male", "Age": 22, "SibSp": 0, "Parch": 0, "Fare": 7.25, "Embarked": "S"}
manager = Manager(path,dic)
print(manager.run())