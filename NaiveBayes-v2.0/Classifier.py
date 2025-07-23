from Log import log
from Trainer import Trainer

class Classifier:
    def __init__(self,df):
        self.df = df
        self.column_to_fill = self.df.columns.to_list()[-1]
        self.trainer = Trainer(self.df)
        self.calculate_data= self.trainer.get_calculate_data()

    def run_validation(self,dic_val):
        res = {}
        for target_value,unique_word_counts in self.calculate_data.items():
            res_num = 1
            for col_value, sum_value in dic_val.items():
                if col_value == self.column_to_fill:
                    continue
                else:
                    res_num *= unique_word_counts[col_value][sum_value]
            res[target_value] = res_num
        res_percentages = self.trainer.get_in_percentages(res)
        log(f"result validation : {res_percentages}")
        return res_percentages