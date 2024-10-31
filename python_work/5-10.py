from random import randint

def guessLoop(num,i=0):
    i += 1
    #新加的失败检测
    if i > 5:
        print("你失败了!!!!!!!!!")
        return i
    #下面是原本的代码
    j = eval(input("输入所猜的数: "))
    if j == num :
        return i
    else :
        if j >= num :
            print("遗憾,太大了")
        else :
            print("遗憾,太小了")
        return guessLoop(num,i)

print("在程序中随机生成了一个 0~9 之间的随机整数")
n = guessLoop(randint(0,9))
if n <= 5:
    print("预测 {N} 次,你猜中了".format(N = n))