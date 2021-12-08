#list of nummbers
listOfStuff = [21,33,77,2,4,10,3,17]

#This loop starts listing the odd and even num from index 7 which is from 17

number_length = len(listOfStuff)
count = 0
print('while loop')
while count < number_length:
  if listOfStuff[count] % 2 == 0:
     print(f"even -{listOfStuff[count]}")
  else:
     print(f"odd -{listOfStuff[count]}")
  count = count + 1

print('----------------------------------------------------------')

#This for loop starts listing the odd and  even odd num fron index 0 which is 21

print('for loop')
listOfStuff =[21,33,77,2,4,10,3,17]
for x in listOfStuff:
   if x % 2 == 0:
    print(f"even -{x}")
   else:
    print(f"odd -{x}")