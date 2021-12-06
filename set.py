listof_fruits={"Orange", "Mango", "Cherry", "Apple", "Pineapple", "Grape"}
print(listof_fruits)

#Add function to list!
listof_fruits.add("Banana")
print(listof_fruits)

#Remove function in sets
listof_fruits.remove("Orange")
print(listof_fruits)

#This is to show that these fruits one is the list and the other is not!
print( "Cherry" in listof_fruits)
print("Strawberry" in listof_fruits)

#Update function in sets.
Food={"Rice","Beans","Plantain"}
Amount={" 500"}
Food.update(Amount)
print(Food)

#This shows that duplicates are not in sets!
listof_fruits={"Orange","Orange","Pineapple","Mango","Grape","Strawberry","Cherry","Apple"," Apple"," Mango"}
print(listof_fruits)
print(type(listof_fruits))