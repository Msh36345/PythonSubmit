import pandas as pd

def col_to_fill(columns):
    for i,col in enumerate(columns):
        print(f"{i+1}. {col}")
    indx_to_fill=int(input("choice column to fill : "))
    return indx_to_fill-1


df = pd.read_csv('/Users/mosheshulman/PycharmProjects/Data/PythonProjectsSubmi/NaiveBayes/data for NB buys computer.csv')

rows=len(df)
columns=df.columns.to_list()

index_column_to_fill = col_to_fill(columns)
columns_for_comparison = columns.copy()
column_to_fill = columns_for_comparison.pop(index_column_to_fill)
print(columns)
print(index_column_to_fill)
print(columns_for_comparison)
print(column_to_fill)





column_word_counts = {}
for col in df.columns:
    counter = (df[col].value_counts(dropna=False)).to_dict()
    counts={}
    for key,val in counter.items():
        if val==0:
            counts[key]=1/rows+1
        else:
            counts[key]=val/rows
    column_word_counts[col] = counts

print(column_word_counts)

inpt={}
for col in columns_for_comparison:
    inpt[col]=input(f"input {col} :")


res={}
for possibility,num in column_word_counts[column_to_fill].items():
    res_num=num
    for key,val in inpt.items():
        res_num*=column_word_counts[key][val]
    res[possibility]=res_num
print(res)



