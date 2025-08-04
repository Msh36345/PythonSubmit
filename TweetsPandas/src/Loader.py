import pandas as pd

class Loader:
    def __init__(self,path):
        self.df =pd.read_csv(path, dtype=str)

    def get_data(self):
        return self.df