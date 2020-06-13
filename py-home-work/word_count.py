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

for inquiry in queries:
    sum_lists = [len(inquiry.split()) for inquiry in queries]

for word, count_word in Counter(sum_lists).items():
    print(f'Поисковых запросов из {word} слов - {round((count_word * 100) / len(queries))} %')