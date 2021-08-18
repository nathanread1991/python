myTuple = (122222, 233333, 3445555, "hello world")

print(myTuple)

print(myTuple[0])

myTuple2 = (myTuple[0], "hello world")

print(myTuple2)

del myTuple

#dictionaries

dict = {"name": "tom", "height": 6.2}
print(dict)
for item in dict:
    print(str(item) + " = " + str(dict[item]))

dict.popitem()

print(dict)

dict.popitem()

print(dict)

dict.clear()

print(dict)

del dict

print(dict)