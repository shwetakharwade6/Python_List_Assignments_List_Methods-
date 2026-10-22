a=[10,20,10,30,20,40,30,50,40,10]
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)
