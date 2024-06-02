pangram = "The quick brown fox jumps over the lazy dog"
numbers = "1838492984827163840332"
numbered_list = [1.4, 2.4, 5.6, 9.0, 5.4]
# The sorted function allows us to sort throu a list, returning an
# itterable list in sorted order
letters = sorted(pangram)
in_order = sorted(numbers)
print(letters)
print(in_order)

numbered_list.sort()
print(numbered_list)
missing_letter = sorted("The quick brown fox jumps over the lazy dog")
print(missing_letter)
