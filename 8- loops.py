# Loops
# python has two primitive loop commands:# for, # while
# for loop is used for iterating over a sequence
# set, tuple, list, dictionary, or string
# eg: for x in listVar:
# we can loop in specific range:
# for i in range(10):
# the default starting value at the range function is 0 but we can specify the starting value by:
# for i in range (2, 10):
# and the default to increment the sequence by 1 but we can specify it by add third parameter:
# for i in range (2, 10, 3):
# we can use else at the loop statement to execute block of codes at the end of loop:
# but if we used break at the loop statement and executed the else statement will not be executed.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number)

print('---------------------------------')
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

print('---------------------------------')
dictVar = dict({
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
})
for key, value in dictVar.items():
    print(key, value)

print('---------------------------------')
str = "Hello World!"
for ch in str:
    print(ch)

print('---------------------------------')
for i in range(10):
    print(i)

print('---------------------------------')
for x in range(5):
    if(x == 2):
        pass
        print(x)
    elif(x == 3):
        continue
    elif(x == 4):
        break
    else:
        print(x)

print('---------------------------------')
for y in range(3):
    pass
    if(y == 2):
        break
else:
    print('Finished ...')

print('---------------------------------')
print('---------------------------------')
j = 1
while j < 10:
    if(j % 8 == 0):
        break
    elif(j % 2 == 1):
        pass
    else:
        print(j)
    j = j + 1
else:
    print('Finished ...')

print('---------------------------------')
a = 1
while a < 3:
    a = a + 1
else:
    print('Finished ...')