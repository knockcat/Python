#print all fibbonacci number less than n

a = 0
b = 1
c = 0
num = int(input("Enter range :"))
while(c<num):
    print(c,end =' ')
    c = a+b
    a = b
    b = c
   
