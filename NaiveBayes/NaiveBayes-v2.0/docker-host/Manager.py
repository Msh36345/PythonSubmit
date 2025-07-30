from Loader import Loader
from Cleaner import Cleaner
from Validator import Validator
from Trainer import Trainer
from Log import log

class Manager:
    def __init__(self,path):
        log("manager host is running...")
        self.loader = Loader(path)
        self.cleaner = Cleaner(self.loader.get_data())
        self.clean_data = self.cleaner.get_clean_data()
        self.validator = Validator(self.clean_data)
        self.accuracy = self.validator.tester()
        self.trainer = Trainer(self.clean_data)
        self.trainer_dic = self.trainer.get_calculate_data()

    def run_testing(self):
        answer = f"The analysis was {self.accuracy} accurate.\nPredicted answer probability:\n"
        for probability,percentages in self.trainer_dic.items():
            answer+=f"          {probability} : {percentages}\n"
        return answer


    def run_host(self):
        answer = str({
            "validator": f"The analysis was {self.accuracy}% accurate for titanic data",
            "calculate_data": self.trainer_dic,
            "col_to_fill": self.validator.column_to_fill
        })
        return answer

