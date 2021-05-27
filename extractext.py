#import os
#file_details = os.pat.splitext('/path/file.ext')
#print(file_details)
#print(file_details[1])
import pathlib
print(pathlib.path('/path/file.ext').suffix)