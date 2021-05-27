from enum import Enum
class Day(Enum):
   monday = 1
   tuesday = 2
   wednesday = 3
print(Day.monday)
print(Day.monday.name)
print(Day.monday.value)