"all of my functions are in this file and you can import this file to use them"

def reverseWords(input=None):
    "you can use the reverseWords functon to reverse the words in a sentence except punctuation"
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = " ".join(inputWords)
    return output

def fibonacciSeries(sum=10):
    "you can use this function to calculate the Fibonacci series "
    a, b = 0, 1
    while b < sum:
        a, b = b, a + b
    return a

def guessNumber(num=5):
    "this is a game called Guess Number"
    guess = -1
    if num not in range(10):
        print("please set a int value from 0 to 10")
    else:
        pass
    while guess != num:
        guess = int(input('please input a number: '))
        if guess > num:
            print('it is too big')
        elif guess < num:
            print('it is too small')
        else:
            print('you are right')

def whileTest():
    i = 0
    while (i <= 10):
        print(i)
        i += 1

def forTest():
    l = ['a', 'b', 'c', 'd', 'e']
    for i in range(5,30,5):
        print(i)
    for i in l:
        print(i)

def findMaxAndMin(*num):
    return max(num), min(num)
    
mySum = lambda num1, num2: num1 + num2