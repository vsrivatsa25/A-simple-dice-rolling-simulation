import random
l = []
n = int(input("Enter number of die throws: "))
for x in range(n):
    l.append(random.randint(1,6))
print("Rolled dice: ",l)
for i in range(1,7):
    print("P({}) = ".format(i),l.count(i)/n)
