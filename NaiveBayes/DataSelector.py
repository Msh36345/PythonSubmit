class DataSelector:

    def __init__(self,data,columns,rows,col_fill):
        self.full_data=data
        self.columns=columns
        self.rows=rows
        self.column_to_fill = col_fill
        self.columns_for_comparison = [col for col in self.columns if col != self.column_to_fill]


    def tester(self,seventy,thirty):
        counter=0
        for row,val in thirty.items():
            check = self.check_row(val,seventy)
            answer=max(check,key=check.get)
            if answer==val[self.column_to_fill]:
                counter+=1
        return (counter / self.rows) * 100

    def ask_for_input(self):
        inpt = {}
        for col in self.columns_for_comparison:
            inpt[col] = input(f"input {col} :")
        print(inpt)
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