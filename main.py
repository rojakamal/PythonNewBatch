#To check 89 is odd or even Number
a = 89
if a % 2 == 1:
    print("Odd Number ")
else:
    print("Even Number")
    print("-------------------------------")

#to print odd numbers between 0 to 100
for i in range(0,101):
    if i % 2 == 1:
        print(i)
print("----------------------------------")

#To Count the odd numbers betweem 0 to 100
count = 0
for i in range(0,101):
    if i %2 == 1:
        count = count + 1
print(count)
print("----------------------------------")

#Sum of odd numbers between 0 to 100
sum = 0
for i in range(0,101):
    if i % 2 == 1:
        sum = sum + i
print(sum)
print("---------------------------------")

#swap a=29,b=67 with 3rd variable
a=29
b=67
temp = 0
print("Before swapping a:",a)
print("Before swapping a:",b)
temp = a
a = b
b = temp
print("After swapping a:",a)
print("After swapping a:",b)
print("---------------------------------")

#swap a=29,b=67  wihtout 3rd variable
a = 29
b = 67
print("Before swapping a:",a)
print("Before swapping a:",b)
a,b=b,a
print("After swapping a:",a)
print("After swapping a:",b)
print("---------------------------------")

a = 29
b = 67
print("Before swapping a:",a)
print("Before swapping a:",b)
a = a+b
b = b-a
a=b-a
print("After swapping a:",a)
print("After swapping a:",b)