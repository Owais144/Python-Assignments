#Q1
"""
num1 = int(input("Enter number one"))
num2 = int(input("Enter number two"))
op = input("Enter operation")

if op == '+':
    print('{}+{} ='.format(num1,num2))
    print(num1 + num2)
elif op == '-':
    print('{}-{} ='.format(num1,num2))
    print(num1 - num2)
elif op == '*':
    print('{}*{} ='.format(num1,num2))
    print(num1 * num2)
elif op == '/':
    print('{}?{} ='.format(num1,num2))
    print(num1/num2)
elif op == 'pow':
    print('{}**{} ='.format(num1,num2))
    print(num1**num2)
"""
#Q2

lst=['a','b','c',1,'d']

for i in lst:
    if i == 1:
        print("numeric exists")

#Q3
"""
d={'one', 'two'}
print(d)
d.update({'three'})
print(d)
"""
#Q4
"""
d = {2,3,4,5}
print(sum(d))
"""
#Q5
"""
a = [1,2,2,4,6,7,1]
seen = {}
dupes = []

for x in a:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1
print(dupes)
"""
#Q6
"""
d = {'one','two'}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present('one')
is_key_present('three')
"""