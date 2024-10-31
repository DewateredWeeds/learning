def isLeapYear(year) :
    if (year % 4) != 0 or ((year % 100) == 0 and (year % 400) != 0) :
        return False
    else :
        return True

year = eval(input("输入一个年份来判断其是否为闰年:"))
if isLeapYear(year) :
    print("这个年份是闰年")
else : print("这个年份不是闰年")

input()