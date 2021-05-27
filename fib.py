nterms = int(input("how many terms"))
n1 , n2 = 0 , 1
count = 2
if nterms <= 0:
    print("please enter a positive integer")
elif nterms == 1:
    print("fibbonacci series upto",nterms,":")
    print(n1)
else:
 print("fibbonacci sequence:")
 print(n1,",",n2,end=',')
 
while count < nterms:
    nth = n1 + n2
    print(nth,end=',')
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1