import json # https://docs.python.org/3/library/json.html
import os
# import glob # https://docs.python.org/3/library/glob.html
import shutil # https://docs.python.org/3/library/shutil.html
import datetime
archive_dir_path = './receipts/archive'

try:
    os.makedirs(archive_dir_path, exist_ok=True)
except FileExistsError as err:
    print(f' \'archive\' dir already exists, error number: {err.errno}, error description: {err.strerror}')
d = datetime.datetime.now()
date_time = d.strftime("d%d%m%Yt%H%Ms%S")
print(date_time)

shutil.make_archive(base_name=f'{archive_dir_path}\\receipts_archive_{date_time}',format='zip', root_dir='./receipts\\processed\\' )

