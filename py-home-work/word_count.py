# В задаче необходимо определить процент поисковых запросов
# в зависимости от количества слов в самом запросе

from collections import Counter

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

sum_lists = []

for inquiry in queries:
    inquiry = len(inquiry.split())
    sum_lists.append(inquiry)

word_dict = dict(Counter(sum_lists))
for word, count_word in word_dict.items():
    print(f'Поисковых запросов из {word} слов - {round((count_word * 100) / len(queries))} %')