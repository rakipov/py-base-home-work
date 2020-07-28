# Происходит сортировка по алфовиту и знакомство с людей с одинковыми индексами
# В случае неравного количества элементов в списке - выводим предупреждение и не знакомим.

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()
    print('Идеальные пары:')
    for i, j in zip(boys, girls):
        print(f"\n{i} и {j}")
else:
    print('Кто-то может остаться без пары!')