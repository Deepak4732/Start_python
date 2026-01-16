#--------------------------------------INPUT()----------------------------------------
# input(): This is used for taking input from the users

a = input()
b = input()
c = a + b
print(c)

# In the above example the input() function takes input from the user is string value and they concatinate a and b in the output 

a = input()
num1 = int(a)
b = input()
num2 = int(b)
c = num1 + num2
print(c)

a = int(input())
b = int(input())
c = a + b
print(c)

# so we can now create a Basic calculater 

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = a + b 
d = a - b
e = a / b
f = a // b
g = a % b

print(f"Addition: {c} \nsubstraction: {d} \nFloat Divide: {e} \n Int Divide: {f} \n Remainder: {g}")

# -----------------------------------TERNARY OPERATOR---------------------------------

x = int(input("Enter first number"))
y = int(input("Enter Second number"))

z = x if x<y else y
print(z)

#-----------------------------------IN OPERATOR---------------------------------------

X = "Aman is Good BOY"
y = "BOY" in X
print(y)

l = [ 1, 12.4, "Suraj"]
m = "u" in l[2][1]
print(m)

#-----------------------------------PRINT()-------------------------------------------

# print create new line after the print executes 
a = 10 
b = 30
print(a)
print(b)

# If we want to use sepration in between the values use sep='@' or anything 

c = 90
print(a,b,c,sep='@')

# if we don't want to create a new line after the execution then we use "end="

print("Hello ",end='p')
print("Baccho ", end='q')
print("Kaise HO", end='r')