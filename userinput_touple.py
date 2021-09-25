#user input touple

t = tuple()

m = int(input('Number of cities you want to enter : '))

for i in range(m):
    a = input('Enter City Name :')
    t = t + (a, )
 

print("Output :",t)
