# f=open('exm.txt','x')
f=open('exm.txt','r')
# print(f.readlines())
a=f.readlines()
l=len(a)
f.seek(0)
for i in range(l):
    b=f.readline().split()
    lar=0
    for j in b:
        if len(j)>=lar:
            lar=len(j)
            larg=j
print(larg)