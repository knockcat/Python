#prime number
num = int(input("Enter a Number: "))
count = 0
for i in range(2,int(num/2)):
    if(num%i == 0):
        count+= 1
        break
if(count < 1):
    print(num,'is prime')
else:
    print(num,'is composite')
