layer = int(input("输入层数:"))
def printa(l):
    for i in range(1,l+1):
        print('*'*i)
    for i in range(0,l):
        print('*'*(l-i))
printa(layer)