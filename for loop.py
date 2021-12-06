#For loop is a control instruction whiich we use for two main purposes: iteration and repetition
#iteration means performing the same action on the different iteams
#For loop statement begins with a "for"
#We include a special variable which represent  each of the list item one at a time(loop control variable)
#We include the "in" keyword which is the connecting key 
#We include the name of the list we'll like to loop over
#We finish with the decleration with the calling that we're entering the for loop
#We include the iteration variable into single indented print statment

my_list= ["A","B","C","D","E","F"]
for x in my_list:
    print(x)

names=["Blessing","Nwanneeka","Munachi"]
for n in names:
    print(n+ ", do you want cash?")
print("yes, i think i want cash ")

for i in range(3):
    print("Baby","Shark", "Do","Do")
print("Mummy", "Shark","Do","Do")

name= "Muna"