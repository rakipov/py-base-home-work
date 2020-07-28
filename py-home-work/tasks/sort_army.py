# Определяем годен ли призывник и в какие войска по росту его можно распределить

age = int(input('Введите свой возраст: '))
height = int(input('Ваш рост: '))
children_count = int(input('Количество детей: '))
studying = input('Являетесь ли вы студентом да/нет: ')

if 18 <= age <= 27  and children_count < 2 and studying == 'нет':
    if 150 <= height < 175:
        print('В танковые войска!')
    elif 150 <= height < 175:
        print('В танковые войска!')
    elif height < 150:
        print('На подлодку!')
    elif 175 <= height <= 185:
        print('В десантники!')
    else:
        print('В другие войска!')
else:
    print('Не годен!')