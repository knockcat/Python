d = {}
l = []
str = input('Enter String :')
l = str.split()

for i in l:
    d[i] = len(i)
ind=[]
for k,v in d.items():
    ind.append((v,k))
ind.sort(reverse=True)
print(ind)







'''
print('Vishal Joshi')
d = {}
l = []
str = input('Enter String :')
l = str.split()
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if len(l[j])<len(l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]

for i in l:
    d[i] = len(i)
    print(i,' : ',len(i),end='  ')
     
'''

