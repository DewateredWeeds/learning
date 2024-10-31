def getA():
    while True:
        a = int(input("输入 a 的值,应为 1~9 的整数: "))
        if (1 <= a <= 9):
            return a
        else:
            print("范围有误,请重新输入")

def getN():
    while True:
        n = int(input("输入 n 的值,应为正整数: "))
        if (n > 0):
            return n
        else:
            print("范围有误,请重新输入")

def getSum(a,n):
    if n > 0:
        return getSum(a,n - 1) + int(str(a) * n)
    else:
        return 0
    
print("和 s 的值为: ",getSum(getA(),getN()))