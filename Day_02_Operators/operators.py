#In python There are 5 types of operators:-  1. Arithmetic operators 2. Relational Operators 3. Assignment operators 4. Bitwise operators and  5.   Logical operators

# ---------------------------Arithmetic operators:----------------------------------- 
#       +, -, *, /, //, %, **

a = 50
b = 5
c = a + b
d = a - b
e = a / b         # gives float value
f = a // b        # gives int value
g = a % b         # gives remainder
h = a ** b        # power a ka power b          
print (c)
print (d)
print (e)
print (f)
print (g)
print (h)

#---------------------------- Relational operator:=-----------------------------------
#       <, >, <=, >=, ==, !=

a = 50
b = 45
c = a > b
d = a < b
e = a <= b
f = a >= b
g = a == b
h = a != b

print (c)
print (d)
print (e)
print (f)
print (g)
print (h)

m = "pankaj" < "payal"      # this is using ASCII code a=97, z=122 and A=65, Z=90 . this is using dictionary to compare which is large or smaller 
print(m)

print(True == 1)

# ----------------------------------Logical Operator----------------------------------

# AND OPERATOR
# A and B: the result is a  if a is false otherwise the result is b

a = 0
b = 12 
c = a and b
print(c)        # the output is Zero that means False 

x = 12
y = 12
z = x and y
print(z)        # here output is 12 depends on second value because 1st is True 

m = 12
n = 0
o = m and n
print (o)

# OR OPERATOR
# A or B : the reult is A when A is True otherwise the result is B.

a = 12
b = 0
c = a or b
print(c)        # here the output is 12 

x = 12
y = 12
z = x or y
print(z)

m = 0
n = 12
o = m or n
print (o)

print("pankaj" or "sharma")
print("" or "sharma")

# NOT OPERATOR
# every operator is reverse when it is true gets false and false gets true

print(not(False))
print(not(True))

#--------------------------------BITWISE OPERATOR-------------------------------------
#       &(bitwise And), |(bitwise OR), ^(XOR), ~(complimentaion), <<(left shift), >>(Right shift)
# Works only in Integer or Boolean 

#   &(bitwise And)
a = 5                   #   0101 - Bitwise of 5
b = 7                   #   0111 - Bitwise of 7
print(a&b)              #   0101 - adding both upper. output is 5

#   |(bitwise OR)
x = 10
y = 15
z = x | y
print(z)

#   ^(XOR)
m = 5                   #   00000101 - Bitwise of 5
n = 7                   #   00000111 - Bitwise of 7
o = m ^ n               #   00000010 - output is 2
print (o)

#   ~(complimentaion)
# ~x = -(x+1)

print(~5)
print(~0)
print(~(-5))

#   <<(left shift)

print(5<<2)         #       0 0 0 0 0 1 0 1 - 5
                    #       / / / / / / / /
                    #    / / / / / / / /
                    #       0 0 0 1 0 1 0 0 output 20

# the formula is x * n ^ 2 

#   >>(Right shift)

print(10>>2)        #       0 0 0 0 1 0 1 0         -  10
                    #        \ \ \ \ \ \ \ \
                    #       0 0 0 0 0 1 0 1
                    #        \ \ \ \ \ \ \ \ 
                    #       0 0 0 0 0 0 0 1 0       output is 2

# formula is n = x // 2^n