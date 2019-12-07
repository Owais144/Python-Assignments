#Q1
"""
def fact():
    num=int(input("Enter number:"))
    factorial = 1
    if num < 0:
        print("Factorial not possible")
    elif num == 0:
        print("The Factorial for 0 is 1")
    else:
        for i in range(1,num+1):
            factorial=factorial*i
        print("The factorial for {} is {}".format(num,factorial))
fact()
"""
#Q2
"""
def Cases():
    inp=input("Enter String : ")
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in inp:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Original String : ",inp)
    print("Number of Upper case letters :",d["UPPER_CASE"]  )
    print("Number of Lower case letters :",d["LOWER_CASE"]  )
Cases()
"""
#Q3
"""
def even():
    lst=[1,2,3,4,5,6,7,8]
    for num in lst:
        if (num%2) == 0:
            print(" ",num)
even()
"""
#Q4
"""
def Palindrome(s):

    rev = ''.join(reversed(s))

    if (s == rev):
        return True
    return False

s = "madam"
ans = Palindrome(s)

if (ans):
    print("Yes")
else:
    print("No")
"""
#Q5
"""
def isPrime(s):
    if s > 1:
        for i in range(2,s):
            if (s%i)==0:
                print(s,"is not a Prime number")
                break
        else:
            print(s,"is a Prime number")
    else:
        print(s, "is Not a Prime number")
isPrime(3)
"""
#Q6
"""
def grocery(*args):
    for arg in args:
        print(arg)
grocery('bread','eggs','milk')
"""
