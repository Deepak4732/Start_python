for i in  range(5): print(i);   # it will execute 0 to 4 because (n-1) at the end 
r = range(1,6)
print(r[2])     # r = 1,2,3,4,5,6 with index 0 to 5. 1 is index 0 and so on. the      index 2 is 3 output.

x= range(5, 40 , 7)

for x in range(7,70,5):        
    print(x)

for x in range(2, 20 ,3):       # so this 2 is start, 20 is end, 3 is step size 
    print(x)

# ----------------------------------------LIST----------------------------------------

l = list(range(5))
print(l)

t = tuple(range(5))
print(t)

l = list("Pankaj")
print(l)


s = {1,4,4.5,"Suraj"}
print(s)                        #Set

print(type(s))
s.add("banana")
print(s)

s.remove("Suraj")
print(s)            

s.add(1)
print(s)        #no duplicate are allowed but it don't gave error.