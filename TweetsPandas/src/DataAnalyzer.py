from collections import Counter

class DataAnalyzer:
    def __init__(self,data):
        self.data = data
        self.antisemitic = self.data[self.data['Biased'] == '1']
        self.non_antisemitic = self.data[self.data['Biased'] == '0']
        self.unspecified = self.data[(self.data['Biased'] != '0') & (self.data['Biased'] != '1')]
        self.lists_data = [self.data,self.antisemitic,self.non_antisemitic]

    def get_sum_tweets(self, data):
        return len(data)

    def get_average(self,data):
        return data["Text"].str.len().mean()

    def get_3_length_tweets(self,data):
        return data.loc[data['Text'].str.len().nlargest(3).index,'Text'].tolist()

    def get_10_most_comments_words(self,data):
        words = self.col_text_to_list(data).lower().split(" ")
        counter_list = Counter(words).most_common(10)
        most_comments_words=""
        for word, count in counter_list:
            most_comments_words+=f"{word}, "
        return most_comments_words[0:-2]

    def get_sum_big_words(self,data):
        words = self.col_text_to_list(data).split(" ")
        count=0
        for word in words:
            if word.isupper():
                count+=1
        return count

    def col_text_to_list(self,data):
        all_words=""
        for row in data['Text']:
            all_words += f"{row} "
        all_words = all_words.replace(",", "").replace(".", "")
        return all_words
