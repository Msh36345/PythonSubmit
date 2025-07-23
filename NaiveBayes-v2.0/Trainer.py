from Log import log


class Trainer:
    def __init__(self,df):
        self.df =df
        self.columns = self.df.columns.to_list()
        self.rows = len(self.df)
        self.column_to_fill = self.columns[-1]


    def get_calculate_data(self):
        final_dic= {}
        # Create a list of all unique values in the target column
        all_target_values = self.df[self.column_to_fill].unique()
        # calculate each unique value in the target column
        for target_value in all_target_values:
            filtered_df = self.df[self.df[self.column_to_fill] == target_value]
            unique_word_counts={}
            for col in self.columns:
                if col==self.column_to_fill:
                    continue
                else:
                    # Create a dictionary where keys are unique values in the column and values are their counts
                    all_col_values = (filtered_df[col].value_counts(dropna=False)).to_dict()
                    counts = {}
                    # Handle missing values
                    for col_value, sum_value in all_col_values.items():
                        if sum_value == 0:
                            counts[col_value] = 1 / self.rows + 1
                        else:
                            counts[col_value] = sum_value / self.rows
                unique_word_counts[col]=counts
            final_dic[target_value] = unique_word_counts
        log(f"final calculate data : {final_dic}")
        return final_dic

    def get_in_percentages(self,dic):
        sum_dic_val=sum(dic.values())
        dic_percentages={}
        for key,val in dic.items():
            percentages=(val / sum_dic_val) * 100
            dic_percentages[key]=f"{round(percentages,2)}%"
        return dic_percentages
