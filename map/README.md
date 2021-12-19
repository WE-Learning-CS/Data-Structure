# Map

- Key - Value를 쌍으로 갖고 있는 자료구조
- 어떠한 데이터 타입도 key값으로 저장이 가능하다.
- 각 쌍의 삽입 순서를 기억하는 자료구조
- key는 중복일 수 없지만 value는 중복일 수 있다.
- key와 value중 하나만 존재하지는 않는다.

# ChainMap

> `ChainMap ` 이라고도 하는 파이썬의 Map은 여러 `dictionary`들을 하나의 단위로 관리하는 데이터 구조이다. 합쳐진 `dictionary`에는 중복 키를 제거하는 키와 값 쌍이 특정 순서로 포함되어 있다. `ChainMap`의 가장 좋은 용도는 한 번에 여러 `dictionary`를 검색하고 적절한 키-값 쌍 매핑을 얻는 것이다. 또한 이러한 `ChainMaps`는 스택 데이터 구조로 동작한다.
>
> 출처 : https://www.tutorialspoint.com/python_data_structure/python_maps.htm

```python
import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps,'\n')
# output : [{'day1': 'Mon', 'day2': 'Tue'}, {'day1': 'Thu', 'day3': 'Wed'}]

print('Keys = {}'.format(list(res.keys())))
# output : Keys = ['day1', 'day3', 'day2']
# key 값은 unique 해야 하므로 두 맵이 중복된 key값을 가질시에는 먼저 삽입된 맵의 데이터를 사용한다.

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

```

## Map update

`dictionary`가 업데이트 되면 `Chainmap`결과도 즉시 업데이트 된다.

```python
## Update Map
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res = collections.ChainMap(dict1, dict2)
print(res.maps,'\n')
# output : [{'day1': 'Mon', 'day2': 'Tue'}, {'day3': 'Wed', 'day4': 'Thu'}] 

dict2['day4'] = 'Fri'
print(res.maps,'\n')
# output : [{'day1': 'Mon', 'day2': 'Tue'}, {'day3': 'Wed', 'day4': 'Fri'}] 
```


