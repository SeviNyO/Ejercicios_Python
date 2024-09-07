#Arithmetic operators

addition = 1 + 1
substraction = 2 - 1
multiplication = 2 * 1
division = 1 / 1
modulus = 3 % 2

#Comparasion operators
true = 2 > 1
false = 1 > 2
equalto = division == multiplication
notEqualTo = true != false

#Logical operators
#  and
#  or
#  not

#Assingment operatorss
#  =
#  +=


#CONDITIONAL STATEMENTS
if 1 == 1:
    print("Equal")
else:
    print("Not Equal")
#Loops FOR and While
iterable = (1,2,3)
for i in iterable:
    print(i)

o = 0
while o < 5:
    print("Hello World")
    o+=1

#Exercise Create a program that prints to the console all the numbers between 10 and 55 (inclusive), that are even, and are neither 16 nor multiples of 3
i = 10
while i < 55:
    if i == 16 or i % 3 == 0:
        i+=1
        continue
    elif i % 2 == 0:
        print(i)
    i+=1