from Log import log

class Cleaner:
    def __init__(self,df):
        self.df=df.drop_duplicates()
        self.drop_index_column()
        self.drop_empty_rows()
        self.log_table_info()

    def get_data(self):
        return self.df

    def drop_index_column(self):
        if "index" in self.df.columns:
            self.df.drop(columns=["index"], inplace=True)
            log("Column index dropped from Data Frame")

    def drop_empty_rows(self):
        self.df.dropna(how='all', inplace=True)

    def log_table_info(self):
        rows, cols = self.df.shape
        log(f"Data Frame cleand | Rows: {rows} | Columns: {cols}")


