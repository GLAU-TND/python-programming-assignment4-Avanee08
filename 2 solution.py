l1=eval(input())
dct={}
for i in l1:
    if l1[i] in range(0,10000):
        dct[i]=l1[i]
    else:
        for j in l1[i]:
            if l1[i][j] in range(0,10000):
                dct[i + '.' + j]=l1[i][j]
            else:
                for k in l1[i][j]:
                    if l1[i][j][k] in range(0,1000000):
                        dct[i+ '.' + j+'.' + k]=l1[i][j][k]
print(dct)                        

