def fib(n):
    if n ==1 or n ==2 :
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
for i in range(1,21):
    print(fib(i),end="\t")
    if i % 5 == 0 :
        print(end="\n")