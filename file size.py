#import os
#file_stat = os.stat('my_file.txt')
#print(file_stat.st_size)
from pathlib import Path
file = Path('my_file.txt')
print(file.stat().st_size)