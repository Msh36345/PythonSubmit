from Log import log
from Trainer import Trainer

class Validator:
    def __init__(self,df):
        self.df = df
        self.calculate_70 = int(len(self.df)*0.7)
        self.column_to_fill = self.df.columns.to_list()[-1]
        log(f"Start testing : train {self.calculate_70} rows | test : {len(self.df)-self.calculate_70} rows")
        self.trainer = Trainer(self.df.iloc[:self.calculate_70])
        self.train_dic = self.trainer.get_calculate_data()
        self.test_dic = self.create_test_df()

    def tester(self):
        counter = 0
        rows_counter = 0
        for row_num, row_val in self.test_dic.items():
            check = self.run_validation(row_val, self.train_dic)
            answer = max(check, key=check.get)
            # log(f"answer row {row_num} : {answer}")
            rows_counter += 1
            if answer == row_val[self.column_to_fill]:
                counter += 1
        log(f"tester result : {counter}/{rows_counter}")
        res = (counter / rows_counter) * 100
        return f"{round(res, 2)}%"

    def run_validation(self,row_val,train_dic):
        res = {}
        for target_value,unique_word_counts in train_dic.items():
            res_num = 1
            for col_value, sum_value in row_val.items():
                if col_value == self.column_to_fill:
                    continue
                else:
                    # res_num *= unique_word_counts[col_value][sum_value]
                    value = unique_word_counts[col_value].get(sum_value, 1e-6)
                    res_num *= value
            res[target_value] = res_num
        return self.trainer.get_in_percentages(res)

    def create_test_df(self):
        thirty_percent_df = self.df.iloc[self.calculate_70:]
        thirty_percent_dict = thirty_percent_df.to_dict(orient='index')
        return thirty_percent_dict
