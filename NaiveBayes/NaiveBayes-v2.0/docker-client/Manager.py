from RequestData import RequestData
from Classifier import Classifier
from Log import log

class Manager:
    def __init__(self,dic_of_row):
        log("manager client is running...")
        self.request = RequestData()
        self.calculate_data= self.request.my_dict["calculate_data"]
        self.classifier = Classifier()
        self.result = self.classifier.run_validation(self.calculate_data,dic_of_row,self.request.my_dict["col_to_fill"])
        self.dic_of_row = dic_of_row

    def run_testing(self):
        answer = f"The analysis was {self.request.my_dict['validator']}% accurate.\nPredicted answer probability:\n"
        for probability,percentages in self.result.items():
            answer+=f"          {probability} : {percentages}\n"
        return answer

    def run(self):
        answer = f"<h3>The analysis was {self.request.my_dict['validator']}% accurate for titanic data.</h3>"
        answer += f"<h4>row to check : {self.dic_of_row}</h4><ul>"
        answer += "<h4>Predicted answer probability:</h4><ul>"
        for probability, percentage in self.result.items():
            answer += f"<li><b>{probability}</b> : {percentage}</li>"
        answer += "</ul>"
        return answer
