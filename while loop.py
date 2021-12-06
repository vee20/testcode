#While loops is basically executing a set of statment as long as the condition is ture
#While condition: do this but when the condition is no longer true then the whule loop ends

x= 1
while x < 5:
    print(x)
    x += 1
print("The end")

a=10
while a < 20:
    print(a)
    a +=10
    print("congratulation")


j= 0
for i in range(6):
    j= j + 2
    print('i= ', i,', j=',j)
    if j==8:
        break
    print("You will see me only if j is not 8")
    print("Congratulation")
