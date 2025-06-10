# dictionary variable
# is type of collection (mapping data type)
# save data as key value pairs
# it is ordered
# it is changeable
# do not allow duplicates
# can create it using {} or dict constructor
# we can access items of dictionary:
# using key like dictVar['one']
# using get method like dictVar.get('one')
# to get all the keys : dictVar.keys()
# to get all the values: dictVar.values()
# and dictVar.items(): return all the items
# check if key exists or not using in
# update dictionary item:
# use key like that: dictVar['one'] = 22
# or use update method: dictVar.update({'one': 22})
# we can use update method to new item: if we use un exits key
# we can add new item like that: dictVar['newKey'] = value
# remove item:
# we can use pop method: take the key
# or popitem method: do not take anything and remove the last entered item
# or use del: del dictVar['one']

dictVar = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
print(dictVar)

dictVar2 = dict(one=1, two=2, three=3, four=4, seven=7, eight=8)
print(dictVar2)

print(dictVar2.get("four"))
print(dictVar['two'])

print(dictVar2.keys())
print(dictVar2.values())
print(dictVar2.items())

print("ten" in dictVar2)

dictVar2["one"] = 11
print(dictVar2)

dictVar2.update({"two": 22})
print(dictVar2)

dictVar2['ten'] = 10
print(dictVar2)

dictVar2.update({'eleven': 111})
print(dictVar2)

dictVar2.pop("eleven")
print(dictVar2)

dictVar2.popitem()
print(dictVar2)

del dictVar2["two"]
print(dictVar2)

for key in dictVar2:
    print(key)
    print(dictVar2[key])

for value in dictVar2.values():
    print(value)

for (key, value) in dictVar2.items():
    print(key, value)