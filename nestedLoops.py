length = 30
astr = "*"
for i in range(length):
    for j in range(length - i):
        print(" ", end='')
    print(astr)
    astr += "**"