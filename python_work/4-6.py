def func(x) :
    if x < 0 :
        return 0.0
    elif x < 5 :
        return x
    elif x < 10 :
        return 3 * x - 5
    elif x < 20 :
        return 0.5 * x - 2
    else :
        return 0.0

print("因变量为:",func(float(input("输入自变量:"))))

input()