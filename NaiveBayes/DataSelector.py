from Log import log
class DataSelector:

    def __init__(self,data,columns,col_fill):
        self.full_data=data
        self.columns=columns
        self.column_to_fill = col_fill
        self.columns_for_comparison = [col for col in self.columns if col != self.column_to_fill]


    def tester(self,seventy,thirty):
        counter=0
        rows_counter=0
        for row,val in thirty.items():
            check = self.check_row(val,seventy)
            answer=max(check,key=check.get)
            log(f"answer row {row} : {answer}")
            rows_counter+=1
            if answer==val[self.column_to_fill]:
                counter+=1
        log(f"{counter}/{rows_counter}")
        res=(counter / rows_counter) * 100
        return f"{round(res,2)}%"

    def ask_for_input(self):
        inpt = {}
        for col in self.columns_for_comparison:
            inpt[col] = input(f"input {col} :")
        log(f"user input : {inpt}")
        res = self.check_row(inpt, self.full_data)
        return res

    def check_row(self,check,data):
        res = {}
        for keyy,vall in data.items():
            res_num = 1
            for possibility, num in check.items():
                if possibility == self.column_to_fill:
                    continue
                else:
                    res_num *= vall[possibility][num]
            res[keyy] = res_num
        return res

    def get_in_percentages(self,dic):
        sumi=sum(dic.values())
        dic_percentages={}
        for key,val in dic.items():
            percentages=(val / sumi) * 100
            dic_percentages[key]=f"{round(percentages,2)}%"
        return dic_percentages