d = {'name': 'hsh', 'age': 22, 'university': 'SEU', 'email': 'its,hushihang@gmail.com','list':[1,2,3,4,5]}
print(d['name'], d['age'])
del d['email']
print(d)

# attention to copy and deepcopy
import copy
d1=d.copy()
d2=copy.deepcopy(d)
print(d1)
print(d2)
d['name'] = 'hhh'
d['list'].remove(1)
print(d1)
print(d2)

print('name' in d)
m = d.items()
print(type(m))
m = list(m)
print(type(m))
print(m)
print(d.values())
print(d.keys())
d.pop('name')
print(d)