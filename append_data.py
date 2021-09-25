
data = input('Enter Data :')

f1 = open('Append.txt','a+')
f1.write(data)
f1.write('\n')

f1.seek(0)

app_data = f1.read()
f1.close()

print(app_data)






