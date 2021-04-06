# create an iterator
class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myNum = myNumbers()
myID = iter(myNum)
print(next(myID))
print(next(myID))
print(next(myID))
print(next(myID))
print(next(myID))
print('-----------------------------------')

# iter
l = [1, 2, 3, 4, 5]
it1 = iter(l)
it2 = iter(l)
it3 = iter(l)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

for x in it2:
    print(x, end=" ")
print('\n-----------------------------')

import sys
print('\t')
while True:
    try:
        print (next(it3),end=" ")
    except StopIteration:
        sys.exit()


# generator
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()