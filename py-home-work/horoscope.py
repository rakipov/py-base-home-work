# Простая задача из первых лекий для определения знака зодиака

day = int(input('Введите день: '))
month = (input('Введите месяц: ')).lower()

if (21 <= day <= 31  and month() == 'март') or (1 <= day <= 20 and month() == 'апрель'):
    print('Ваш знак зодика "Овен"')
elif (21 <= day <= 30  and month() == 'апрель') or (1 <= day <= 20 and month() == 'май'):
    print('Ваш знак зодика "Телец"')
elif (21 <= day <= 31  and month() == 'май') or (1 <= day <= 21 and month() == 'июнь'):
    print('Ваш знак зодика "Блезнецы"')
elif (22 <= day <= 30  and month() == 'июнь') or (1 <= day <= 22 and month() == 'июль'):
    print('Ваш знак зодика "Рак"')
elif (23 <= day <= 31  and month() == 'июль') or (1 <= day <= 23 and month() == 'август'):
    print('Ваш знак зодика "Лев"')
elif (24 <= day <= 31  and month() == 'август') or (1 <= day <= 23 and month() == 'сентябрь'):
    print('Ваш знак зодика "Дева"')
elif (24 <= day <= 30  and month() == 'сентябрь') or (1 <= day <= 23 and month() == 'октябрь'):
    print('Ваш знак зодика "Весы"')
elif (24 <= day <= 31  and month() == 'октябрь') or (1 <= day <= 22 and month() == 'ноябрь'):
    print('Ваш знак зодика "Скорпион"')
elif (23 <= day <= 30  and month() == 'ноябрь') or (1 <= day <= 21 and month() == 'декабрь'):
    print('Ваш знак зодика "Стрелец"')
elif (22 <= day <= 31  and month() == 'декабрь') or (1 <= day <= 20 and month() == 'январь'):
    print('Ваш знак зодика "Козерог"')
elif (21 <= day <= 31  and month() == 'январь') or (1 <= day <= 18 and month() == 'февраль'):
    print('Ваш знак зодика "Водолей"')
elif (19 <= day <= 29  and month() == 'февраль') or (1 <= day <= 20 and month() == 'март'):
    print('Ваш знак зодика "Рыбы"')
else:
    print('Введите корретные дату и месяц!')