from nums import *
from add import *
from sub import *
from mul import *
from div import *
from mod import *
from floor import *
from exp import *
while True:
    print(
        '''
1.Add
2.Sub
3.Mul
4.Div
5.Modulus
6.Floor div
7.Exponent
8.Exit
'''
    )
    ch=int(input('Enter your choice : '))
    if ch==1:
        a,b=nums()
        add(a,b)
    elif ch==2:
        a,b=nums()
        sub(a,b)
    elif ch==3:
        a,b=nums()
        mul(a,b)
    elif ch==4:
        a,b=nums()
        div(a,b)
    elif ch==5:
        a,b=nums()
        mod(a,b)
    elif ch==6:
        a,b=nums()
        floor(a,b)
    elif ch==7:
        a,b=nums()
        exp(a,b)
    elif ch==8:
        break
    else:
        print('Invalid choice')