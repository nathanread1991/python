import json # https://docs.python.org/3/library/json.html
import os
import glob # https://docs.python.org/3/library/glob.html
import shutil # https://docs.python.org/3/library/shutil.html
try:
    os.mkdir('./receipts/processed')
except OSError:
    print('processed dir already exists')

# receipts = [glob.replace('./','') for glob in glob.glob('./receipts/new/receipt-[0-9]*.json')]
receipts = glob.glob('./receipts/new/receipt-[0-9]*.json')
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')[-1].replace('new\\', '')
    print(name)
    destination = f'./receipts\\processed\\{name}'
    shutil.move(src=path, dst=destination)
    print(f'processing file {name}')
print(receipts)

print(f'Receipt subtotal:£{subtotal:.2f}')
