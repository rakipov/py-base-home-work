stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

for key_stats, max_value in stats.items():
    if max_value == max(stats.values()):
        print(f'Максимальные продажи: {key_stats}')