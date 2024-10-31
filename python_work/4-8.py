x = eval(input("输入 x 坐标:"))
y = eval(input("输入 y 坐标:"))

if x > 0 :
    if y > 0 :
        print("点在第一象限")
    elif y < 0 :
        print("点在第四象限")
    else :
        print("点在 x 轴正方向")
elif x < 0 :
    if y > 0 :
        print("点在第二象限")
    elif y < 0 :
        print("点在第三象限")
    else :
        print("点在 x 轴负方向")
else :
    if y > 0 :
        print("点在 y 轴正方向")
    elif y < 0 :
        print("点在 y 轴负方向")
    else :
        print("点在原点上")

input()