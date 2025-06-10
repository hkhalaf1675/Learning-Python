# tuple variable
# it is type of sequence
# it is like array at other languages or list at python
# the tuple can carry any type of data not one type
# subscriptable: allow access items
# Allow duplicates
# can create or declare it using the () or tuple constructor
# the first item at tuple has index of 0
# can access the items using negative numbers (the -1 refer to the last item, the -2 refer to the second last item)
# can access range of tuple items using tupleVar[2:4],
# or tupleVar[2:] to get from the third item to the last item,
# or tupleVar[:-1] to get from the first item to the second item from the last
# unchangeable: can not change, add, remove items of it
# we can convert the tuple to list using list constructor and convert the list to tuple use the tuple constructor
# unpacking tuple:
# like destruction at javascript
# (one, two, three) = tupleVar

tupleVar = ("one", "two", "three", "four", "five")
print(tupleVar)

print(tupleVar[0])
print(tupleVar[1: 4])

tupleVar2 = tuple((1, 2, 4, 3, 5, 8, 6, 5))
print(tupleVar2)
print(tupleVar2[-1])
print(tupleVar2[1: -2])

(one, two, three, four, five) = tupleVar
print(one)

numOfTimes = tupleVar2.count(5)
print(numOfTimes)

indexOfItem = tupleVar2.index(5)
print(indexOfItem)