#def get_permutation(string, i=0):
  # if i == len(string):
 #     print("",join(string))
#for j in range(i, len(string)):
  #  words = [c for c in string]
 #   words[i], words[j] = words[j], words[i]
#
 #   get_permutation(words, i + 1)
#print(get_permutation('yup'))
from itertools import permutations
words =['',join(p) for p in permutations('prog')]
print(words)