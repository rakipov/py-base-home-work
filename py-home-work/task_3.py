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

# queries = len(queries)
# print(queries)

sum_lists = []

for inquiry in queries:
    inquiry = list(''.join(inquiry).split())
    inquiry = len(inquiry)
    sum_lists.append(inquiry)
# print(sum_lists)

fin = dict(Counter(sum_lists))


