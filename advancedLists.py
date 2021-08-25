import argparse


parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete string to search for in words')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('dict.txt') as f:
    words = f.readlines()

# for word in words:
#     if snippet in word.lower():
#         matches.append(word)
# print(matches)
# list comprehensions https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
matches = [word.strip() for word in words if snippet in word.lower()]
print(matches)

for match in matches:
    print(match, end=' ')


