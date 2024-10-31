def isPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return(False)
    return(True)

max = int(input("输入最大值寻找素数:"))

count = 0

for i in range(3,max):
    if isPrime(i):
        print(i,end='\t')
        count += 1

print('\n',"总共有",count,"个素数")
    