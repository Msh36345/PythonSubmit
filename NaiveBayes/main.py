from DataLoader import DataLoader
from DataSelector import DataSelector

class Manager:
    def __init__(self,path):
        self.data=DataLoader(path,self.ask_column_to_fill())
        self.col=self.data.get_columns()
        self.rows=self.data.get_rows()
        self.full_data=self.data.get_full_data()
        self.seven=self.data.get_seventy_percent()
        self.tree=self.data.get_thirty_percent_rows()
        self.col_fill=self.data.column_to_fill
        self.sel=DataSelector(self.full_data,self.col,self.col_fill)
        self.menu()

    def tester(self):
        result = self.sel.tester(self.seven, self.tree)
        print("Result tester :", result)

    def input_data(self):
        res = self.sel.ask_for_input()
        print(self.sel.get_in_percentages(res))

    def ask_column_to_fill(self):
        inpt = input("Would you like to choose a column to fill? True/False : ").strip().lower()
        return inpt == "true"

    def menu(self):
        print("""======================
||  1. tester       ||
||  2. input data   ||
||  0. exit         ||
======================""")
        choice = input("select your choice :")
        if choice=="1":
            self.tester()
        elif choice=="2":
            self.input_data()
        elif choice=="0":
            print("bye bye!!")
            return
        else:
            print("Invalid choice")
            self.menu()


# path = '/Users/mosheshulman/PycharmProjects/Data/PythonProjectsSubmi/NaiveBayes/csv/buys computer.csv'
path='/Users/mosheshulman/PycharmProjects/Data/PythonProjectsSubmi/NaiveBayes/csv/phishing.csv'
Manager(path)