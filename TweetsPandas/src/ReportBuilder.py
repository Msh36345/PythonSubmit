from DataAnalyzer import DataAnalyzer

class ReportBuilder:
    def __init__(self,data):
        self.analyzer = DataAnalyzer(data)
        self.all_df = {"total" : self.analyzer.data,
                         "antisemitic" : self.analyzer.antisemitic,
                         "non_antisemitic" : self.analyzer.non_antisemitic,
                         "unspecified" : self.analyzer.unspecified}
        self.df_types = ["total", "antisemitic", "non_antisemitic", "unspecified"]
        self.dic_report = {"total_tweets" : self.get_total_tweets(),
                    "average_length" : self.get_average_length(),
                    "common_words": self.get_common_words(),
                    "longest_3_tweets" : self.longest_3_tweets(),
                    "uppercase_words": self.uppercase_words()}

    def get_total_tweets(self):
        dic_total_tweets = {}
        for df_type in self.df_types:
            dic_total_tweets[df_type] = self.analyzer.get_sum_tweets(self.all_df[df_type])
        return dic_total_tweets

    def get_average_length(self):
        dic_average_length = {}
        for df_type in self.df_types[:3]:
            dic_average_length[df_type] = self.analyzer.get_average(self.all_df[df_type])
        return dic_average_length

    def get_common_words(self):
        dic_common_words = {}
        for df_type in self.df_types[:1]:
            dic_common_words[df_type] = self.analyzer.get_10_most_comments_words(self.all_df[df_type])
        return dic_common_words

    def longest_3_tweets(self):
        dic_longest_3_tweets = {}
        for df_type in self.df_types[1:3]:
            dic_longest_3_tweets[df_type] = self.analyzer.get_3_length_tweets(self.all_df[df_type])
        return dic_longest_3_tweets

    def uppercase_words(self):
        dic_uppercase_words = {}
        for df_type in self.df_types[:3]:
            dic_uppercase_words[df_type] = self.analyzer.get_sum_big_words(self.all_df[df_type])
        return dic_uppercase_words
