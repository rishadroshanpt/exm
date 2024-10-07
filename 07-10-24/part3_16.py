def swap(d1,d2):
    for i in d1:
        t=i
        i=d1[i]
        d2[i]=t
    print(d2)
d2={}
d1={'name':'appu','age':21}
swap(d1,d2)