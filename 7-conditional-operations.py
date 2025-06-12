# we use (if, elif, else) to make condition
# to check equality between two variables (if var1 == var2)
# to check not equality (if var1 != var2)
# to compare between two variables (if var1 > var2, if var1 < var2, var1 >= var2, …)
# to opposite condition (if not var1 > var2)
# to aggregate between two or more condition (if var1 > var2 [and, or] var2 == var3)
# use or: if one condition is true , then all the if statement will be true
# use and: must be all condition be true, to execute the if statement

x = 40
y = 50
if x == y:
    print("x is equal to y")
elif x != y:
    print("x is not equal to y")

a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

pi = 3.15
if not pi == 3.14: print("pi does not have correct value")

if pi > 3 and pi < 4: print("pi have almost the correct value")

if x > y or a > b:
    print("x is greater than or equal to y")
elif not (x > y or a > b):
    print("x is not greater than or equal to y")

for i in range(10):
    if(i % 2 == 0):
        pass
    else:
        print(i)
