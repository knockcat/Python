#if-elif
per = float(input("Enter your percentage"))
if(per>75):
    print('A')
elif(per<75) and (per>60):
    print('B')
elif(per<60) and (per>50):
    print('C')
elif(per<50) and (per>40):
    print('D')
else:
    print('F')
