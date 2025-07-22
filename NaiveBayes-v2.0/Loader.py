import pandas as pd
from Log import log

class Loader:

    def __init__(self,path):
        self.df = pd.read_csv(path)
        self.path = path

    def get_data(self):
        return self.df

    def log_table_info(self):
        rows, cols = self.df.shape
        log(f"Data Frame create from '{self.path}' | Rows: {rows} | Columns: {cols}")

