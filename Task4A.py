import random

f1 = open("data1.txt", "w") #opening file in read mode
for i in range(1000): #10000 numberbers are going to feed
    number=str(random.randint(0,1000)) #creating random numberber in range 0-1000 and converting it to string
    f1.write(number)   
    f1.write("\n")
f1.close