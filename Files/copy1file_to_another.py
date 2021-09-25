f1 = open('data.txt','r')
data = f1.read()
print(data)

f2 = open('copydata.txt','w')
data2 =f2.write(data)
print(data)
