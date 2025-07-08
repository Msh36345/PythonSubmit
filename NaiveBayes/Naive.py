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
        counts[key]=val/rows
    column_word_counts[col] = counts

print(f"rows : {rows}")
for col, counts in column_word_counts.items():
    print(f"\ncol: {col}")
    for word, count in counts.items():
        print(f"{word}: {count}")

inpt={}
for col in columns_for_comparison:
    inpt[col]=input(f"input {col} :")


