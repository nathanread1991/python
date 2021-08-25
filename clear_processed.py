import glob  # https://docs.python.org/3/library/glob.html
import os

file_list = glob.glob('./receipts/processed/receipt-[0-9]*.json')

print(file_list)

for file in file_list:
    try:
        os.remove(file)
    except OSError as e:
        print(f'Error: {e.filename} - {e.strerror}')
    else:
        print(f'deleting file {file}')
