'''program to prints the integers from 1 to 100 .
But for multiple of three print :Fizz" instead of the number ,
and for the multiples of five print "buzz".
For numbers which are multiple of both three and five print "FizzBuzz" '''
'''
for i in range(0,101):
    
    
    if((i%3 != 0) and (i%5 != 0)):
        print(i,end = ' ')
    elif((i%3 == 0) and i%5 == 0):
        print("FizzBuzz",end = ' ')
    if(i%3 == 0 and i%5 != 0):
         print("Fizz",end = ' ')
    elif(i%5 == 0 and i%3 != 0):
        print("Buzz",end = ' ')
        '''

'''
for index,value in enumerate(st): 
    print(index,'-',value)
'''
for i in range(1,101):
    #print(i,end = ' ')
    
    if((i%3 != 0) and (i%5 != 0)):
        print(i,end = ' ')
    elif((i%3 == 0) and i%5 == 0):
        print("FizzBuzz",end = ' ')
    elif(i%3 == 0):
         print("Fizz",end = ' ')
    elif(i%5 == 0):
        print("Buzz",end = ' ')
