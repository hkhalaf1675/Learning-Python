# set variable
# it is type of sequence
# it is like array at other languages or list at python
# the list can carry any type of data not one type
# do not allow duplicates
# can create or declare it using the {} or set constructor
# unordered: mean that the items in a set do not have a defined order
# unchangeable: can not change items of it
# unsubscriptable: allow access items using [] like setVar[0]
# but we can access items using for in loop
# we can check if item exists at the set using in: eg if "one" in setVar
# we can add new items to the set using add method
# we can add sets or any iterable object using update method
# we can remove item from the set using remove or discard method
# the two method take the value and search about it and delete it
# but the remove method will raise an error if there is no items exits with the entered value but the discard will not
# we can use clear method to remove all the set items
# we can use pop: but it will delete random item
# can loop through the list using (for in)


setVar = {1, 2, 7, 3, 4, 6, "five"}
print(setVar)

setVar2 = set(("one", "two", "three", "four", "five"))
print(setVar2)

for item in setVar:
    print(item)

setVar.add("seven")
print(setVar)

setVar.update(setVar2)
print(setVar)

setVar.discard("seven")
print(setVar)

setVar.remove("five")
print(setVar)