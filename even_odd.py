#This code iterate through every number in a list to separate out even and odd number
list_of_numbers= [1,2,3,4,5,6,7,21,33,2,4]
even_numbers= []
odd_numbers = []
for number in list_of_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else: 
        odd_numbers.append(number) 
print(even_numbers)
print(odd_numbers)

