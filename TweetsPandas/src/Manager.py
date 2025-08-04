from Loader import Loader
from DataAnalyzer import DataAnalyzer
from DataCleaner import DataCleaner


class Manager:
    def __init__(self,path):
        self.loader = Loader(path)
        self.data = self.loader.get_data()
        self.analyzer = DataAnalyzer(self.data)
        self.antisemitic = self.analyzer.antisemitic
        self.non_antisemitic = self.analyzer.non_antisemitic
        self.cleaner = DataCleaner(self.data)
        self.clean_df = self.cleaner.clean_data
        # self.clean_df.to_csv("clean.csv", index=False)



if __name__ == "__main__":
    manager = Manager("/Users/mosheshulman/PycharmProjects/Data/PythonProjectsSubmi/TweetsPandas/data/tweets_dataset.csv")


