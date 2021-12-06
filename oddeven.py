#list of numbers
#For loop
#listOfStuff = [21,33,77,2,4,10,3,17]
#for x in listOfStuff:
  #  if x % 2 == 0:
     #   print(f"even- {x}")
    #else:
       # print(f"odd- {x}")
# While loop
listOfStuff = [21,33,77,2,4,10,3,17]
count = len(listOfStuff)

while count > 0: 
    count = count - 1
    if listOfStuff[count] % 2 == 0:
      print(f" even {listOfStuff[count]}")
else:
        print(f"odd {listOfStuff[count]}")