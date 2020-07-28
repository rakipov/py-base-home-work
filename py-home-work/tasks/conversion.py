my_list = ['2018-01-01', 'yandex', 'cpc', 100]

my_dict = {}

value = my_list.pop()
final_key = my_list[-1]
for key in reversed(my_list):
    my_dict = {key: my_dict}
    if key == final_key:
        my_dict.update({final_key: value})
print(my_dict)