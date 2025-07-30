from Log import log

class Cleaner:
    def __init__(self,df):
        self.df=df.drop_duplicates()
        self.drop_index_column()
        self.df = self.df.sample(frac=1, random_state=42)
        self.drop_empty_rows()
        self.convert_all_to_str()
        self.log_table_info()

    def get_clean_data(self):
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

    def convert_all_to_str(self):
        self.df = self.df.applymap(lambda x: str(x) if isinstance(x, (int, float)) else x)
        log("All int and float values converted to string in Data Frame")


