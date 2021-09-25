print('Malkeet Singh')
f1 = open('Quote.txt','r')
data = f1.read()
count = 1
for i in data:
    if i == ' '  :
         count += 1

print(data)
print('Number of words in the file (''Quote.txt'') is :',count)
