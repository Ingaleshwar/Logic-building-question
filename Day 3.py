# 1> Check for Armstrong number - A number is called an Armstrong number 
# if the sum of its own digits each raised to the power of the number of digits is equal to the number itself.

num=int(input("Enter a number to check it's armstrong number or not: "))

def arm_strong(num):
    len_num = len(str(num))
    n=num
    sum=0
    while(num>0):
        digit=num%10
        sum+= digit**len_num
        num//=10
    if(n==sum):
        print("Yes the number is Armstrong number!")
    else:
        print("The number is not Armstrong number!")
    
arm_strong(num) 

# 2> Check for Perfect number
num=int(input("Enter a number to check it is perfect number: "))
def perfect_num(num):
    if(num<=0):
        print("Only positive intergers!")
        return None
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    return sum==num

if (perfect_num(num)):
    print("The number is perfect number!")
else: 
    print("The number is not a perfect number!")

# 3> Calculate simple interest
p=float(input("Enter the principle amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter time/duration in years: "))
def S_I(p,r,t):
    return ((p*r*t)/100)
print(S_I(p,r,t))

# 4 Find power of a number (without **)
print("Enter base number and exponent number to find it's power: ")
base_num=int(input("Enter the base number: "))
exp_num=int(input("Enter the exponent number: "))
def pow(base_num,exp_num):
    power=1
    for i in range(1,exp_num+1):
        power*=base_num
    return power
print("The power of the given base number and exponent number is: ",pow(base_num,exp_num))

# 5 Check if a character is a vowel or consonant
ch=input("Enter a character to check if it is Vowel or consonant: ")
def char(ch):
    vow=['a','e','i','o','u']
    if ch.lower() in vow:
        print("It is a Vowel!")
    else:
        print("It is consonant!")
char(ch)

# 6 Find the largest digit in a number
num=int(input("Enter a number to find the largest digit in it: "))
def lg_digi(num):
    large=0
    while num>0:
        digit=num%10
        if(large<digit):
            large=digit
        num//=10
    return large

print("The largest digit is: ",lg_digi(num))
