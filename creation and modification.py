#import os.path. time
#file = pathlib.path('abc.py')
#print("last modification time: %s" % time.ctime(os.path.getmtime(file)))
#print("last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))
import datetime
import pathlib
fname = pathlib.path('abc.py')
print("last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("last metdata change timeor path creation time: %s" %datetime.datetime.fromtimestamp(fname.stat().st_ctime))
