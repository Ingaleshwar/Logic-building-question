# 1> Check if a number is a palindrome 
num=int(input("Enter a number to check it's palindrome or not: "))
def ispalindrome(num):
    rev=0
    temp=num
    if(num<0): 
        print("Invaild, input!")
    else:
        while(temp>0):
            digit=temp%10
            rev=rev*10+digit
            temp//=10
    return (num==rev)
print(ispalindrome(num))

# 2> Check if a number is prime 
num= int(input("Enter a number to check it's prime or not: "))
def prime_no(num):
    prime=True
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            prime=False
            break
    if(not prime or num<=1):
        return False
    else:
        return True
print(prime_no(num))

# 3> Generate Fibonacci series
num=int(input("Enter the number of Terms: "))
def fib(num):
    a,b=0,1
    if(num<=0):
        print("Enter postive intergers only!!!")
    elif(num==1):
        print(f"{"The fibonacci series is"}, {a}")
    else:
        print("The Fibonacci series is: ")
        print(a,b,end=" ")
        for i in range(2,num):
            c=a+b
            print(c,end=' ')
            a,b=b,c
fib(num)

# 4> Find GCD of two numbers
# 5> Find LCM of two numbers
# 6> Count the number of digits in a number
# 7> Sum of digits of a number
# 8> Convert binary to decimal
# 9> Convert decimal to binary
# 10> Count vowels in a string
# 11> Reverse a string
# 12> Convert Roman numerals to integer
# 13> Convert integer to Roman numeral