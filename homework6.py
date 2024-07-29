my_dict = dict(name='Evgeniy', age=29, location=dict(country='Russia', city='Sochi'))

print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict["name"]}')
print(f'Not existing value: {my_dict.get("planet")}')

my_dict.update({'phone': 88005553535, 'mail': 'runvasyarun38@mail.ru'})

print(f'Deleted value: {my_dict.pop("phone")}')
print(f'Modified dictionary: {my_dict}')


my_set = {True, 'True', 'Истина', 'True', True}
print(f'Set: {my_set}')
my_set.add(False)
my_set.add('False')
my_set.add('Ложь')
my_set.discard('Ложь')
print(f'Modified set: {my_set}')
