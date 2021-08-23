import argparse
# Build the parser
parser = argparse.ArgumentParser(description='Reads a file in reverse', prog='file reverse')
parser.add_argument('filename', help='the file to read in')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s: v1.0')
parser.add_argument('--mode', '-m', choices=['create', 'read', 'update', 'delete'])
args = parser.parse_args()

with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]
    for line in lines:
        print(line.strip()[::-1])
# Parse the arguments
print(args)

# Read the file, reverse the contents and print
