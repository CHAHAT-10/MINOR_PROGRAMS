index = [1, 2, 3]
languages = ['python', 'c', 'c++']
#dictionary = dict(zip(index, languages))
dictionary = {k: v for k, v in zip(index, languages)}
print(dictionary)