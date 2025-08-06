# 1> WAP to swap two numbers
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("The swaped numbers are:", n1, n2)

# 2> Check if a number is odd or even 
n=int(input("Enter a number to check a number is even or odd: "))
if(n%2==0):
    print("Number is Even")
else:
    print("Number is Odd")
    
# 3> Find the largest of three numbers 
n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
n3=int(input("Enter a number: "))
if(n1>=n2 and n1>=n3):
    print(n1, "is largest")
elif(n2>=n1 and n2>=n3):
    print(n2," is Largest")
else:
    print(n3, "is largest")
    
# 4> Print numbers from 1 to N 
n=int(input("Enter a number to print from 1 to N: "))
for i in range(1,n+1):
    print(i,end=' ')
print()

# 5> Sum of N natural numbers 
n = int(input("Enter a number to find the sum of natural numbers: "))
sum=0
if(n>0):
    for i in range(1,n+1):
        sum+=i
    print(sum)

else:
    print("Enter a Natural Number")
    
# 6> Print Multiplication table
n=int(input("Enter a number to know it's multiples from 1 to 10: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

# 7>Find a Factorial of a number 
n=int(input("Enter a number to find it's factorial: "))
mul=1
if(n<0):
    print("Invaild number!")
elif(n==0 or n==1):
    print("Factorial is 1")
else:
    for i in range(1,n+1):
        mul*=i
    print("Factorial of ",n," is", mul)
    
    
# 8> Check if a year is leap or !
yr=int(input("Enter a year to find it is leap yr ot not: "))
if (yr % 400 == 0) or (yr % 4 == 0 and yr % 100 != 0):
    print("Entered yr is leap year!")
else:
    print("Not a leap year")
    
    
# 9> Convert Celsius to Fahrenhiet 
temp=int(input("Enter the temperature to convert it from Celsius to Fahrenhiet: "))
f=(temp*9/5)+32
print(f, " F")

# 10> Reverse a given number
num=int(input("Enter a number to print it's reverse format: "))
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num//=10

print("The reverse of entered number is", rev)