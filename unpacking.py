a = b = c = d = e = f = 12  # All six variables are bound to the 
# same value = 12
print(c)

x, y, z = (1, 2, 3) # Packed tuple
print(x)
print(y)
print(z)
print(x,y,z)

print("Unpacking a tuple")

data = (1,2,76) # data represents a tuple 
x,y,z = data
print(x)
print(y)
print(z)

print("Unpacking a list") # Tuple unpacked

data_list = [12, 13, 14] # Lists can have variables assigned example

p,q,r = data_list # Packed list

print(p)
print(q)
print(r)
