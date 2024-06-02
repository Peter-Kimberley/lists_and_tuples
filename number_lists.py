even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(even)
another_even = even 
print(another_even)
print()
even.extend(odd)
print(even)
print(id(even))
even.sort(reverse=True)
print(even)
print(id(even))
