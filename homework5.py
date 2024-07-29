immutable_var = ('Hello', ['World', '!'], 5)
print(immutable_var)

try:
    immutable_var[0] = 'Goodbye'
    print(immutable_var)
except TypeError as err:
    print(f'\nОшибка: {err}\nТип переменной immutable_var: {type(immutable_var)} - неизменяемый тип)\n')

mutable_list = [1, 2, 3, 'four']
print(mutable_list)

mutable_list[0] = 'один'
print(mutable_list)
