import xml.etree.ElementTree as ET
from collections import Counter


def get_top_ten_word(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    news_list = root.findall('channel/item/description')
    news_word = list()
    for title in news_list:
        news_title_list = title.text.split(' ')
        for word in news_title_list:
            if len(word) > 6:
                news_word.append(word)
    top_ten_word = Counter(news_word).most_common(10)
    for num, xml_unit in enumerate(top_ten_word):
        print(num + 1, xml_unit[0], '\n')


get_top_ten_word('files/newsafr.xml')
