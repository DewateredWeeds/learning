grade = [("优",90),("良",80),("中",70),("及格",60),("不及格",0)]

def getGrade(score,i = 0) :
    if i >= len(grade) :
        return grade[-1][0]
    elif score >= grade[i][1] :
        return grade[i][0]
    else :
        return getGrade(score,i + 1)
    
print("分数评级为:",getGrade(eval(input("输入分数以评级:"))))

input()