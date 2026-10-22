a=[30,10,20,10]

a.append(40)
print("append:",a)

a.insert(1,50)
print("insert:",a)

a.remove(10)
print("remove:",a)

a.pop()
print("pop:",a)

print("count:",a.count(10))
print("index:",a.index(20))

b=a.copy()
print("copy:",b)

a.extend([60,70])
print("extend:",a)

a.sort()
print("sort:",a)

a.reverse()
print("reverse:",a)

a.clear()
print("clear:",a)
