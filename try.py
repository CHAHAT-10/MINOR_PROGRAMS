string = input()

try:
   num = int(input())
   print(string+num)
except (typeerror, valueerror) as e:
    print(e)  