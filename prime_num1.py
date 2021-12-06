#Prime number is a number that can divide only one and itself without reminder.EG 2,3,7....
# This code prints all the numbers between 1o and 20 except prime number.

#METHOD 1

#Create the list of numbers!
list_of_numbers = list(range(10,21))
print(list_of_numbers)

#Create a set to add the non_prime_numbers
non_prime_numbers =set()

#iterate through the list and select the non prime numbers
for number in list_of_numbers:
    for x in range(2, number):
        if (number % x) == 0:
         non_prime_numbers.add(number)
print(non_prime_numbers)
