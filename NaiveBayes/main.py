from DataLoader import DataLoader
from DataSelector import DataSelector

# data = DataLoader('/Users/mosheshulman/PycharmProjects/Data/PythonProjectsSubmi/NaiveBayes/csv/buys computer.csv')
data=DataLoader('/Users/mosheshulman/PycharmProjects/Data/PythonProjectsSubmi/NaiveBayes/csv/phishing.csv')
col=data.get_columns()
rows=data.get_rows()
full_data=data.get_full_data()
seven=data.get_seventy_percent()
tree=data.get_thirty_percent_rows()
col_fill=data.column_to_fill

sel=DataSelector(full_data,col,rows,col_fill)
result = sel.tester(seven, tree)
print("Result:", result)
# res = sel.ask_for_input()
# print(sel.get_in_percentages(res))