f1 = open('Num.txt','w+')
for i in range(0,10):
           num = int(input('Enter Number -: '))
           f1.write(str(num))
           f1.write(' ')

f1.seek(0)

f2 = open('NumSort.txt','w+')
data = f1.read()
l = []

print('Content of Num.txt :',data)

nums = data.split()

for i in nums:
    l.append(int(i))

l.sort()
f2.write(str(l))
print('List after Sorting ->',l)

f1.close()
f2.close()
