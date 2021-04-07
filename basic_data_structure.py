# use list as stack
stack=[1,2,3,4,5]
print(stack)
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
stack.pop()
stack.pop()
print(stack)
print('--------------------------------------------------------------')

# use list as queue
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(type(queue))
print(queue)
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
queue.popleft()                 # The first to arrive now leaves
queue.popleft()
queue.popleft()
print(queue)
print('--------------------------------------------------------------')

# list comprehension

l1=[1,2,3,4,5]
print(l1)
l2=[2*i for i in l1]
print(l2)
l3=[[i,2*i,3*i] for i in l1]
print(l3)
l4=[i for i in l1 if i<=3]
print(l4)
l5=[i+j for i in l1 for j in l2]
print(l5)
print('--------------------------------------------------------------')

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
matrixT=[[row[i] for row in matrix] for i in range(4)]
print(matrix)
print(matrixT)