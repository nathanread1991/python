x = 0
while x < 10:
    print(x)
    x += 1

for item in range(1, 19):
    print(item)

myList = ["nathan", "jason", "natasha", "katie"]

for item in myList:
    print(item.upper())

myName = "Nathan Read"

for char in myName:
    print(char)

for i in range(0, 20):
    if i == 8:
        continue #break
        print("in if: ", i)
    print(i)

for i in range(0, 20):
    if i == 8:
        break
        print("in if: ", i)
    print(i)

for i in range(0, 20):
    if i == 8:
        pass
        print("in if: ", i)
    print(i)