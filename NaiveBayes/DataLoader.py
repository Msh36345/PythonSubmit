import pandas as pd
from Log import log

class DataLoader:

    def __init__(self,path):
        self.df = pd.read_csv(path)
        self.rows = len(self.df)
        self.columns = self.df.columns.to_list()
        self.column_to_fill = self.columns[self.ask_column_to_fill()]

        
    def ask_column_to_fill(self):
        for i, col in enumerate(self.columns):
            print(f"{i + 1}. {col}")
        index_to_fill = int(input("choice column to fill : "))
        return index_to_fill - 1

    def get_rows(self):
        log(f"rows : {self.rows}")
        return self.rows

    def get_columns(self):
        log(f"columns : {self.columns}")
        return self.columns


    def get_full_data(self):
        column_word_counts = {}
        target_values = self.df[self.column_to_fill].unique()
        for unique in target_values:
            filtered_df = self.df[self.df[self.column_to_fill] == unique]
            unique_word_counts={}
            for col in self.columns:
                if col==self.column_to_fill:
                    continue
                else:
                    counter = (filtered_df[col].value_counts(dropna=False)).to_dict()
                    counts = {}
                    for key, val in counter.items():
                        if val == 0:
                            counts[key] = 1 / self.rows + 1
                        else:
                            counts[key] = val / self.rows
                unique_word_counts[col]=counts
            column_word_counts[unique] = unique_word_counts
        log(f"data : {column_word_counts}")
        return column_word_counts

    def get_seventy_percent(self):
        seventy_percent_count = int(self.rows * 0.7)
        filtered_df = self.df.iloc[:seventy_percent_count]
        column_word_counts = {}
        target_values = filtered_df[self.column_to_fill].unique()
        for unique in target_values:
            sub_df = filtered_df[filtered_df[self.column_to_fill] == unique]
            unique_word_counts = {}
            for col in self.columns:
                if col == self.column_to_fill:
                    continue
                else:
                    counter = (sub_df[col].value_counts(dropna=False)).to_dict()
                    counts = {}
                    for key, val in counter.items():
                        if val == 0:
                            counts[key] = 1 / self.rows + 1
                        else:
                            counts[key] = val / self.rows
                    unique_word_counts[col] = counts
            column_word_counts[unique] = unique_word_counts
        log(f"70 percent of data : {column_word_counts}")
        return column_word_counts

    def get_thirty_percent_rows(self):
        seventy_percent_count = int(self.rows * 0.7)
        thirty_percent_df = self.df.iloc[seventy_percent_count:]
        thirty_percent_dict = thirty_percent_df.to_dict(orient='index')
        log(f"30 percent of rows data : {thirty_percent_dict}")
        return thirty_percent_dict
