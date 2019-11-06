#Sum/Average Program
#Nikhil Ramesh
#1300571


numberlist = []
for x in range (0,20):
    anumber = int(input("enter number:"))
    numberlist.append(anumber)

#list sum average

sumint=0
for x in range(0,20):
    sumint = sumint + numberlist[x]
print("the sum of all the numbers you entered is:")
print(sumint)

#for avg of numbers 

for x in range(0,20):
    avgint = int(sumint/20)
print("the average of numbers you entered is:")
print(avgint)
