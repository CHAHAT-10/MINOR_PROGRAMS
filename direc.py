import os
try:
   os.makedirs("/dirA/dirB")
except FileExistsError:
    print("file already exists")