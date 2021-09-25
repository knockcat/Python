#print all prime number in given range A to B


A = int(input("Enter starting point : "))

B = int(input("Enter ending point : "))

for i in range(A,B+1):
        if(i>1):
            for j in range(2,int(i/2)):
                if(i%j == 0):
                    flag = 0
                    break
            else:
                print(i)
