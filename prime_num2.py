#METHOD 2
#Create the list of numbers!

list_of_numbers =list(range(10,21))
print(list_of_numbers)

#list a list to append non prime numbers
non_prime_numbers = []

#iterate through the list and select the non prime numbers

for number in list_of_numbers:
    for x in range(2, number):
        if(number % x)== 0:
            non_prime_numbers.append(number)
            break
print(non_prime_numbers)