'''
import math
l=[]
prime=[]
while True:
    n=input("Enter : ")
    if(n=='END'):
        break
    else:
        l.append(int(n))
for i in range(len(l)):
    c=0
    for j in range(2,(int(math.sqrt(l[i])))+1):
        if(l[i]%j==0):
            c=1
            break
    if(l[i]>1 and c==0):
        prime.append(l[i])
print(prime)

'''
print('Vishal Joshi')
l = []
prime = []
cnt = 0
while True:
    num = input('enter : ')
    if (num == 'END'):
        break;
   
    l.append(num)

for i  in range(len(l)):
    l[i] = int(l[i])
print(l)

for i in l:
    if i>1:
        
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                break
        else:
              prime.append(i)
                   
print(prime)


'''
l = []
prime = []

while 1:
    num = input('enter : ')
    if (num == 'END'):
        break;
    else:
        l.append(int(num))
print(l)

for i in range(0,len(l)):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if (i%j == 0):
                break
            else:
                prime.append(i)
    
print(prime)
'''





'''l = []
prime = []
while 1:
    num = input('enter : ')
    if (num == 'END'):
        break;
    else:
        l.append(int(num))
        
for i in l:
        for j in range(2,int(num)):
            if(i%j == 0):
                break
            else:
                prime.append(i)

print(prime)
'''

'''
l=[]
while True:
    a=input("Enter the numbers and enter END to exit\n")
    if a=="END":
        break
    else:
        c,i=0,2
        b=int(a)
        while i<=(b//2):
            if b%i==0:
                c=c+1
            
            i=i+1
        if c==0:
            l.append(b)

print("The numbers in list: ",l)'''






