import json
from collections import Counter


def get_top_ten_word_for_json(file_path):
    with open(file_path) as file:
        news_list = json.load(file)
        news_word_for_json = list()
    for news in news_list['rss']['channel']['items']:
        news_title_list = news['description'].split(' ')
        for word in news_title_list:
            if len(word) > 6:
                news_word_for_json.append(word)
        top_ten_word = Counter(news_word_for_json).most_common(10)
    for num, json_unit in enumerate(top_ten_word):
        print(num + 1, json_unit[0], '\n')


get_top_ten_word_for_json('../files/newsafr.json')
