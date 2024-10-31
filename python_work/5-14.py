#num = n * 9
#num % 2 == 1(not needed,num = n*2*2*2+1)
#num % 4 == 1
#num % 5 == 1
#num > 9
#num <- [63,63+126..]
#num % 8 == 1
#num = n*7*9 = n*7*3*3

i = 63
while True:
    i += 126
    if i % 4 == 1 and i % 5 == 1 and i % 7 == 0 and i % 8 == 1:
        break

print("糖果至少有 {num} 个".format(num = i))