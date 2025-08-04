from Loader import Loader
from DataCleaner import DataCleaner
from ReportBuilder import ReportBuilder
import DataExporter

class Manager:
    def __init__(self,path):
        self.loader = Loader(path)
        self.data = self.loader.get_data()
        self.report = ReportBuilder(self.data)
        self.cleaner = DataCleaner(self.data)
        self.clean_df = self.cleaner.clean_data

    def export_csv(self):
        DataExporter.export_to_csv(self.clean_df,"tweets_dataset_cleaned")

    def export_json(self):
        DataExporter.export_to_json(self.report.dic_report,"results")




if __name__ == "__main__":
    manager = Manager("/Users/mosheshulman/PycharmProjects/Data/PythonProjectsSubmi/TweetsPandas/data/tweets_dataset.csv")
    manager.export_csv()
    manager.export_json()

