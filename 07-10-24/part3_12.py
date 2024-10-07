l1=[1,2,4,4,5,2,6,3]
l2=[]
for i in l1:
    if i in l2:
        continue
    else:
        l2.append(i)
print(l1)
print(l2)