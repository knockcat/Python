#add temp only if no entry is done for the day
temp = {}
def addDailyTemp(day,avg_temp):
   
    if (day,avg_temp) not in temp:
         temp[day] = avg_temp
              
    return temp

for i in range(0,3):
    day = input('Enter Day of Week :')
    avg_temp = float(input('Average temp of week :'))
    temp = addDailyTemp(day,avg_temp)

print(temp)
         








'''
def addDailyTemp(l):
    temp = {}
    for (day,avg_temp) in l:
          if (day,avg_temp) not in temp:
              temp[day] = avg_temp
    return temp

l = []
for i in range(0,3):
    day = input('Enter Day of Week :')
    avg_temp = float(input('Average temp of week :'))
    l.append((day,avg_temp))
    
temp = addDailyTemp(l)


print(temp)
'''
