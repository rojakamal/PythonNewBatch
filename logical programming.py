num = 252
rev = 0
while num>0:
    rem = num%10
    rev = rev*10 + rem
    num = num//10
print(rev)
print("-----------------")

num = 252
temp = num
rev = 0
while num>0:
    rem = num%10
    rev = rev*10 + rem
    num =num//10
print(rev)
if temp ==rev:
     print("palindrome number")
else:
     print("not a palindrome number")
print("-------------------")

num=252
count = 0
while num>0:
    count = count+1
    num=num//10
print(count)
print("------------------")

num = 252
sum = 0
while num>0:
    rem = num%10
    sum = sum+rem
    num = num//10
print(sum)
print("------------------")

num=371
temp=num
res=0
while num>0:
    rem = num%10
    res = res+rem**3
    num=num//10
print(res)
if temp==res:
    print("Amstrong Number")
else:
    print("not Armstrong Number")
print("---------------------")

num = 67
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"not a prime number")
            break
        else:
            print(num,"prime number")
            break
print("---------------------")

num = 8
fact = 1
while num>0:
    fact = fact*num
    num = num-1
print(fact)
print("---------------------")

s ="hello"
count = 0
for i in s:
    count = count+1
print(count)
print("--------------------")

s = "Hello"
count = 0
x = s.split(' ')
for i in x:
    print(i)
    count = count+1
print(count)
print("--------------------")

s = "Hello"
vowels = ['a','e','i','o','u','A','E','I','O','U']
count =0
for i in s:
    if i in vowels:
        count = count+1
print(count)
print("---------------------")

s= "hello"
n = len(s)
rev = " "
for i in range(n-1,-1,-1):
    rev = rev+s[i]
print(rev)
if s==rev:
    print("string is palindrome")
else:
    print("string is not a palindrome")