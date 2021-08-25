import random
import json
import os

count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open('dict.txt').readlines()]

for identifier in range(count):
    amount = random.uniform(1,10000)
    content = {
        'topic': random.choice(words),
        'value': f'{amount:.2f}'
    }
    with open(f'./receipts/new/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)
