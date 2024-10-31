def fac(num):
    if num == 1 :
        return 1
    else :
        return num * fac(num - 1)
print("阶乘为:",fac(eval(input("输入数字:"))))