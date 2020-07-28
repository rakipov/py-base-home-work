# Простая задача из первых лекий для определения знака зодиака

day = int(input('Введите день: '))
month = (input('Введите месяц: ')).lower()
if day <= 31:
    if (21 <= day <= 31 and month == 'март') or (1 <= day <= 20 and month == 'апрель'):
        zodiac = 'Овен'
    elif (21 <= day <= 30 and month == 'апрель') or (1 <= day <= 20 and month == 'май'):
        zodiac = 'Телец'
    elif (21 <= day <= 31 and month == 'май') or (1 <= day <= 21 and month == 'июнь'):
        zodiac = 'Блезнецы'
    elif (22 <= day <= 30 and month == 'июнь') or (1 <= day <= 22 and month == 'июль'):
        zodiac = 'Рак'
    elif (23 <= day <= 31 and month == 'июль') or (1 <= day <= 23 and month == 'август'):
        zodiac = 'Лев'
    elif (24 <= day <= 31 and month == 'август') or (1 <= day <= 23 and month == 'сентябрь'):
        zodiac = 'Дева'
    elif (24 <= day <= 30 and month == 'сентябрь') or (1 <= day <= 23 and month == 'октябрь'):
        zodiac = 'Весы'
    elif (24 <= day <= 31 and month == 'октябрь') or (1 <= day <= 22 and month == 'ноябрь'):
        zodiac = 'Скорпион'
    elif (23 <= day <= 30 and month == 'ноябрь') or (1 <= day <= 21 and month == 'декабрь'):
        zodiac = 'Стрелец'
    elif (22 <= day <= 31 and month == 'декабрь') or (1 <= day <= 20 and month == 'январь'):
        zodiac = 'Козерог'
    elif (21 <= day <= 31 and month == 'январь') or (1 <= day <= 18 and month == 'февраль'):
        zodiac = 'Водолей'
    elif (19 <= day <= 29 and month == 'февраль') or (1 <= day <= 20 and month == 'март'):
        zodiac = 'Рыбы'
    print(f'Ваш знак зодиака: {zodiac}')
else:
    print('Введите корретные дату и месяц!')
