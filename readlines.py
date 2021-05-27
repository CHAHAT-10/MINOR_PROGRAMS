#with open("data_file.txt") as f:
  #  content_list = f.readlines()
#print(content_list)
#content_list = [x.strip() for x in content_list]
#print(content_list) 
with open('data_file.txt') as f:
    content_list = [line for line in f]
print(content_list)
with open('data_file.txt') as f:
    content_list = [line.rstrip() for line in f]
print(content_list)    
