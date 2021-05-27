def recr_fibo(n):
    if n <= 1:
        return n
    else:
        return(recr_fibo(n-1) + recr_fibo(n-2))    
nterms = 10
if nterms <= 0:
    print("please enter a positive number")
else:
    print("fibbonacci sequence")
for i in range(nterms):
    print(recr_fibo(i))