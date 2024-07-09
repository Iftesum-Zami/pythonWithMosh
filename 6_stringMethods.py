course = 'Python for Beginners'
print(len(course))  # also counts spaces

# specific functions to string (method)
print(course.upper())
print(course.lower())

print(course)  # methods dont change the original string

print(course.find('o'))  # case sensitive
print(course.find('Beginners'))  # will give the starting index

print(course.replace('Beginners', 'Absolute Beginners'))  # contains two parameters, 1st old and 2nd new

print('Python' in course)  # "in" is a reserved word. Checks if the 'Python' string is in course variable. Returns a boolean

# applying method vs in operator
