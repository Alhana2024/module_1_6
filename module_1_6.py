my_dict = {'Ivan' : 1973, 'Olga' : 1969, 'Yulia' : 1975, 'Frank' : 1960}
print('My dict:', my_dict)
print('Existing value:', my_dict['Frank'])
print('Not existing value:', my_dict.get('Sean'))
my_dict.update({'Sean':1959, 'Nat': 1971})
a = my_dict.pop('Ivan')
print('Deleted value: ', a)
print('Modified dictionary:', my_dict)
my_set = {5, 1, 2.22, 2.22, True, 'cup', 'cup', 5}
print('Set:', my_set)
my_set.add('element')
my_set.add((5, 3, 5))
my_set.remove(2.22)
print('Modyfied set:', my_set)
