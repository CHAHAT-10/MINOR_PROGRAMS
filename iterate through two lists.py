import itertools
list_1 = [1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c', 'd', 'e']
#for i, j in zip(list_1, list_2):
#    print(i, j)
for i, j in itertools.izip(list_1, list_2):
    print(i,j)
print("\n")
for i,j in itertools.izip_longest(list_1, list_2):
    print (i,j)