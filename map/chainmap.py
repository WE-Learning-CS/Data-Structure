'''
출처 : https://www.tutorialspoint.com/python_data_structure/python_maps.htm
'''

import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps,'\n')
# output : [{'day1': 'Mon', 'day2': 'Tue'}, {'day1': 'Thu', 'day3': 'Wed'}]

print('Keys = {}'.format(list(res.keys())))
# output : Keys = ['day1', 'day3', 'day2']

print('Values = {}'.format(list(res.values())))
# output : Values = ['Mon', 'Wed', 'Tue']
print()

# Print all the elements from the result
print('elements:')
for key, val in res.items():
   print('{} = {}'.format(key, val))
print()

'''
elements:
day1 = Mon
day3 = Wed
day2 = Tue
'''

# Find a specific value in the result
print('day3 in res: {}'.format(('day1' in res)))
# output : day3 in res: True

print('day4 in res: {}'.format(('day4' in res)))
# output : day4 in res: False

## Update Map
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res = collections.ChainMap(dict1, dict2)
print(res.maps,'\n')
# output : [{'day1': 'Mon', 'day2': 'Tue'}, {'day3': 'Wed', 'day4': 'Thu'}] 

dict2['day4'] = 'Fri'
print(res.maps,'\n')
# output : [{'day1': 'Mon', 'day2': 'Tue'}, {'day3': 'Wed', 'day4': 'Fri'}] 
