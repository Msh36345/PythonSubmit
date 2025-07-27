import pandas as pd
from Log import log

class Loader:

    def __init__(self,path):
        self.df = pd.read_csv(path)
        self.log_table_info(path)

    def get_data(self):
        return self.df

    def log_table_info(self,path):
        rows, cols = self.df.shape
        log(f"Data Frame create from '{path}' | Rows: {rows} | Columns: {cols}")

