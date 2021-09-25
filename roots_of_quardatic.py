import math
a = int(input('Enter value of cofficient a :'))
b = int(input('Enter value of cofficient b :'))
c = int(input('Enter value of cofficient c :'))

d = b*b - (4*a*c)

if d > 0:
    print('Real and different roots')
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print('value of root 1 = ',r1, 'Value of root 2 =',r2)

elif d == 0:
    r1 = r2 = -b / (2*a)
    print('Two Equal and Real Roots')
    print('Value of root 1 = ',r1, 'Value of root 2 =',r2)

else:
    print('Complex Roots')
    r1 = r2 = -b / (2*a)
    img = math.sqrt(abs(d)) / (2*a)
    print('Value of root 1 = ',r1, '+ i' , img,'and Value root 2  = ',r2, '- i' , img)
