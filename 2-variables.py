
# python is dynamic language
# there is six types of variable at python

# string variable
strVar = "Hello Python!"
print('"', str, '" is of type: ', type(strVar))

# numeric variables:
# integer
intVar = 3
print('"', intVar, '" is of type: ', type(intVar))

# float
floatVar = 3.14
print('"', floatVar, '" is of type: ', type(floatVar))

# complex
complexVar = 3.14j
print('"', complexVar, '" is of type: ', type(complexVar))

# Sequence variables
# list
listVar = [1, "two", 'three']
print('"', listVar, '" is of type: ', type(listVar))

# tuple
tupleVar = ("tow", 'three')
print('"', tupleVar, '" is of type: ', type(tupleVar))
# tupleVar[0] = "tow" # will give an error because tuple does not support assignment (can not change there values like constant)

# set
setVar = {1, 2, 3}
print('"', setVar, '" is of type: ', type(setVar))
# setVar[0] = "one" # will give an error because tuple does not support assignment and subscriptable(can not change there values like tuple)

# mapping variables
# dictionary
dictVar = {'one': 1, 'two': 2, 'three': 3}
print('"', dictVar, '" is of type: ', type(dictVar))

# boolean variable
boolVar = True
print('"', boolVar, '" is of type: ', type(boolVar))