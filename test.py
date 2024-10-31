f = lambda x:eval(input(x))
def main(m,n):
    print("求和为",m+n,"\n","平均为",(m+n)/2)
main(int(f("请输入第一个参数: ")),int(f("请输入第二个参数: ")))
input()