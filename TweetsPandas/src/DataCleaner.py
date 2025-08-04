class DataCleaner:
    def __init__(self,data):
        self.data = data
        self.clean_data = self.data[self.data['Biased' == '0' or '1']]
        self.data_cleaner()

    def data_cleaner(self):
        for row in self.clean_data:
            self.remove_Punctuation_marks(row)
            self.convert_to_lower(row)

    def remove_Punctuation_marks(self,row):
        row['Text'] = row['Text'].replace("." or "," or ":","")

    def convert_to_lower(self,row):
        row['Text'] = row['Text'].lower()





