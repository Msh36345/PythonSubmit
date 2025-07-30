from Loader import Loader
from Cleaner import Cleaner
from Validator import Validator
from Classifier import Classifier
from Log import log

class Manager:
    def __init__(self,path,dic_of_row):
        log("manager is running...")
        self.loader = Loader(path)
        self.cleaner = Cleaner(self.loader.get_data())
        self.clean_data = self.cleaner.get_clean_data()
        self.validator = Validator(self.clean_data)
        self.accuracy = self.validator.tester()
        self.classifier = Classifier(self.clean_data)
        self.result = self.classifier.run_validation(dic_of_row)

    def run_testing(self):
        answer = f"The analysis was {self.accuracy}% accurate.\nPredicted answer probability:\n"
        for probability,percentages in self.result.items():
            answer+=f"          {probability} : {percentages}\n"
        return answer

    def run(self):
        answer = f"<h3>The analysis was {self.accuracy}% accurate for titanic data.</h3>"
        answer += "<h4>Predicted answer probability:</h4><ul>"
        for probability, percentage in self.result.items():
            answer += f"<li><b>{probability}</b> : {percentage}</li>"
        answer += "</ul>"
        return answer

