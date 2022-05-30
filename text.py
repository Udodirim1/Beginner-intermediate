# customer_id = input('enter a customer id: ')
# if customer_id.find(",") == -1:
#     print(customer_id.split())
# else:
#     print('ERROR')


key = list(summary.keys())
inside_dictionary = summary[key[0]]
inside_dictionary = dict(sorted(inside_dictionary.items(), key=lambda key_value: key_value[0]))
for key, value in inside_dictionary.items():
    print(f'{key}: {value}')