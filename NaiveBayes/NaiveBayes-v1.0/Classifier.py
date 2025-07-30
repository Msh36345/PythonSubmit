from Log import log
from Trainer import Trainer

class Classifier:
    def __init__(self,df):
        self.df = df
        self.column_to_fill = self.df.columns.to_list()[-1]
        self.trainer = Trainer(self.df)
        self.calculate_data= self.trainer.get_calculate_data()

    def run_validation(self,dic_of_row):
        res = {}
        for target_value,unique_word_counts in self.calculate_data.items():
            res_num = 1
            for col_value, sum_value in dic_of_row.items():
                if col_value == self.column_to_fill:
                    continue
                else:
                    # res_num *= unique_word_counts[col_value][sum_value]
                    value = unique_word_counts[col_value].get(sum_value, 1e-6)
                    res_num *= value
            res[target_value] = res_num
        res_percentages = self.trainer.get_in_percentages(res)
        log(f"result validation : {res_percentages}")
        return res_percentages