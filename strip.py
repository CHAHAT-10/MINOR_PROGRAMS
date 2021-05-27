#my_string = "phython"
#print(my_string.strip())
#my_string = " \npython "
#print(my_string.strip(""))
import re
my_string = " hello python "
output = re.sub(r'^\s+|\s+$', '', my_string)
print(output)