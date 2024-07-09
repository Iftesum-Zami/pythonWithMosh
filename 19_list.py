names = ["John", "Bob", "Mosh", "Sara", "Marry"]
print(names)
print(names[2])
print(names[-2])
print(names[1:4])
print(names[-4:-1])
print(names[:])   # exactly like strings

print(names)  # above operations don't change our original list

names[0] = "Sina"
print(names)  # this will change our list
