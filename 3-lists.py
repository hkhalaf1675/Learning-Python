# list variable
# it is type of sequence
# it is like array at other languages
# the list can carry any type of data not one type
# changeable: allow change, add, remove items of it
# subscriptable: allow access items
# Allow duplicates
# can create or declare it using the [] or list constructor
# the first item at list has index of 0
# can access the items using negative numbers (the -1 refer to the last item, the -2 refer to the second last item)
# can access range of list items using listVar[2:4],
# or listVar[2:] to get from the third item to the last item,
# or listVar[:-1] to get from the first item to the second item from the last
# can check if item exists at the list using in
# we can insert new item at specific place at the list using insert
# or can add new item at the last of the list using append
# can remove item from list using one of those ways
# use pop: take the index of the item
# use remove: take the value of the item (and if there is more than one item with that value will remove the first occurrence
# use del: like del listVar[0]
# use del with only the name of the list will delete the list
# use clear method: to remove all list items
# can loop through the list using (for in), (for in range), (while)
# can sort list:
# using sort method: to sort the items alphanumerically, asc be default
# to sort desc: use at the sort method reverse=True
# the sort method can take the function of sorting
# to reverse the the ordering of list items: we can use reverse method
# we can copy list items using: copy method, or list constructor, or slice op listVar[:]

listVar = [1, "two", "three", True, False, [5, 6]]
listVar2 = list((33, 44, "Fifty five"))
print(listVar)
print(listVar2)

listVar[1] = "Two"

print('value of first item at the list: ', listVar[0])
print('value of last item at the list: ', listVar2[-1])
print('the items from second from first to the second from the last is: ', listVar[1: -2])

listVar2[1: 3] = ["thirty three", "forty four"]
listVar2[1: 3] = ["thirty three-forty four"]

print("three" in listVar)

listVar.insert(3, "list inserted")
listVar2.append("list appended")

for item in listVar:
    print(item)

i = 0
for i in range(len(listVar2)):
    print(listVar2[i])
    i = i + 1

i = 0
while i < len(listVar2):
    print(listVar2[i])
    i = i + 1

print('-------------------------')
listVar3 = [1, 5, 3, 5, 8, 2]
print(listVar3)
listVar3.sort()
print(listVar3)
listVar3.sort(reverse=True)
print(listVar3)

listVar4 = list(('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'))
print(listVar4)
listVar4.reverse()
print(listVar4)