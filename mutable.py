shopping_list = ["pasta" ,
                 "milk" ,
                 "eggs"
                 ]


another_list = shopping_list


print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]

print(shopping_list)
print(id(shopping_list))

a = b = c = d = e = f = another_list

print(id(a)) 
print(id(b))


print(id(c))
print(id(d))
print(id(e))

print(a)
print()
print(b)
print()
print("adding cream")
print()
c.append("cream")
print(c)
print()
print(d)
print()
print(e)


