# Q.1- Reverse the list.

a=int(input("Enter element in list"))
print("Enter the elements")
l=[]
for i in range(0,a):
    s=int(input())
    l.append(s)
print(l)
print("reversed")
l.reverse()
print(l)

# Q.2- extract all the uppercase letters from a string.

print("Enter string")
x=input()
str=""
for i in x:
    if(i.isupper()==True):
        str=str +i
print("uppercase: ",str)

# Q.3- Split and store the values after typecasting

a=input("Enter no ")
x=[]
x=a.split(",")
print(x)

# Q.4- Check the palindrome.

print("Enter a string")
a=input()
r="".join(reversed(a))
print(a,r)
if(a==r):
    print("Palindromic")
else:
    print("Not Palindromic")
    
# Q.5- understand Deep and Shallow Copy.

# DeepCopy
import copy
x=[6,3,[4,9],14,16,90]
y=copy.deepcopy(x)
print('List 1: ',x)
print('List 2(deepcopy of list 1): ',y)
y[2][1]=39
print('After changing List 2')
print('List 1: ',x)
print('List 2(deepcopy of list 1): ',y)
print(" ")


#DIFFERENCE
'''
Changes made in deep copy of a list are never reflected in the original list
where as changes made in shallow copy of a list are always reflected in original
list.
In deep copy copy of object is copied to other object where as in shallow copy
reference of object is copied in other object
'''1
