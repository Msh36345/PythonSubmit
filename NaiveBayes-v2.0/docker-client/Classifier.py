from Log import log
from RequestData import RequestData

class Classifier:

    def run_validation(self,calculate_data,dic_of_row,col_to_fill):
        res = {}
        for target_value,unique_word_counts in calculate_data.items():
            res_num = 1
            for col_value, sum_value in dic_of_row.items():
                if col_value == col_to_fill:
                    continue
                else:
                    value = unique_word_counts[col_value].get(sum_value, 1e-6)
                    res_num *= value
            res[target_value] = res_num
        res_percentages = self.get_in_percentages(res)
        log(f"result validation : {res_percentages}")
        return res_percentages

    def get_in_percentages(self,dic):
        sum_dic_val=sum(dic.values())
        dic_percentages={}
        for key,val in dic.items():
            percentages=(val / sum_dic_val) * 100
            dic_percentages[key]=f"{round(percentages,2)}%"
        return dic_percentages