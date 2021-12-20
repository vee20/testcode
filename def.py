#This code iterate through every number in a list to separate out even and odd number
listOfNumbers = [1,2,3,4,5,6,7,21,33,2,4]
def evenOddNumber():
    even_numbers =[]
    odd_numbers = []
    for number in listOfNumbers:
       if number % 2 == 0:
          even_numbers.append(number)
       else: 
          odd_numbers.append(number)
    print(f"{even_numbers}")
    print(f"{odd_numbers}")

evenOddNumber()
