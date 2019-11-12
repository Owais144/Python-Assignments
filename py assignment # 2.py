#Q1
"""

print("Enter marks out of 20")
sub1 = int(input("Enter subject one marks ="))
sub2 = int(input("Enter subject two marks ="))
sub3 = int(input("Enter subject three marks ="))
sub4 = int(input("Enter subject four marks ="))
sub5 = int(input("Enter subject five marks ="))
Total = sub1 + sub2 + sub3 + sub4 + sub5
print("Total marks ="+str(Total))
if Total >=90:
    print("A Grade")
elif Total <=85:
    print("B Grade")
elif Total <=75:
    print("C Grade")
elif Total <=65:
    print("D Grade")
else:
    print("FAIL")
"""
#Q2
"""

num1 = int(input("Enter number"))

if num1 % 2 ==0 :
    print("The number is even")
else:
    print("The number is odd")
"""
#Q3
"""
lst = ["one",'two','three','four','five']
print(len(lst))
"""
#Q4
"""
lst1 = [1,2,3,4,5]
print(sum(lst1))
"""
#Q5
"""
lst2 = [1,2,3,4,5]
print(max(lst2))
"""
#Q6
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a :
    if i < 5:
        print(i)
"""
