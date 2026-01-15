"""
x= "Welcome to my coding center"
print(x[2:6]) #counting starts with 0 and exclude the last one ex = welcome has 6 letters and i exclude 2 and 6 then ans will "lcom"

"""
"""
x="hello world"
print(x.upper()) # this will turns into upper case 
print(x.lower()) # this will turns into lower case 

"""

x = "     Hello world    "
#print(x) #It will gave white spaces in the output 
#print(x.strip()) #remove all spaces in the output

#print(x.replace("H","P")) # Replace the value into any you have provided in that code  
print(x.replace("H","P",).replace("e","i"))


"""
a="hello"
b="world"
#c=a+b   # the output will be helloworld not space in between them. 
c = a + " " + b # it will give a simple space in the string
print(c)  

"""
"""
x = 23 
text = "My name is Deepak kumar and I am {} years old " # { } this curly brases is known for placeholder
print(text.format(x)) # .format(x) is use to add the value in it 

# and { } this place holder is also use in multiple stored value in one example is below 

quantity = 10
order = "burger" 
price = 400

text = "He ordered {} {} and his price is {}, please pay the money"
print(text.format(quantity, order, price ))

# and we also use this kind of 

quantity = 10
order = "burger" 
price = 400

text = "He ordered {0} {1} and his price is {2}, please pay the money"
print(text.format(quantity, order, price ))

# okey Insted of doing this we use this 

quant = 10
odr = "burger" 
pr = 400

text = f"He ordered {quant} {odr} and his price is {pr}, please pay the money"
print(text)

# this is super duper looks preety amazing 

"""
import sys
print(sys.version)