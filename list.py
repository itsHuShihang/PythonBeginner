l=[1,2,3,4,5,6,7,8]
print(l)
del l[2]
print(l)
print(len(l))
for i in l:
    print(i)
print(max(l))
print(min(l))

# convert tuple to l
t=(1,2,3,4,5)
print(type(t))
t2l=list(t)
print(type(t2l))
print(t2l)

# methods of the list
ll=['a','b','c']
print(l)
l.append(9)
print(l)
print(l.count(4))
l.extend(ll)
print(l)
print(l.index(4))
l.insert(2,'new')
print(l)
print(l.pop(2))
print(l)
l.remove('a')
print(l)
l.reverse()
print(l)
l3 = l.copy()
print(l3)
l3.clear()
print(l3)