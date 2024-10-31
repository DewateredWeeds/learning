number = input("请输入一个三位整数:")
if len(number) == 3 and type(eval(number)) == int:
    print("这个三位数的反序数为:"+number[2]+number[1]+number[0])
else: print("输入的不是一个三位整数")
