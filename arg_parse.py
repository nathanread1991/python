import sys

print(f"First argument {sys.argv[0]}")
print(sys.argv[1:])
for arg in sys.argv:
    print(arg)

print(sys.argv[3])