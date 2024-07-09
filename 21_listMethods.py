numbers = [5, 2, 1, 5, 7, 4]

numbers.append(20)  # to add 20 in the last
numbers.insert(2, 8)  # takes 2 parameter, 1st is index, 2nd is the number we wanna append
numbers.remove(1)
# numbers.clear()  # removes all element
numbers.pop()  # removes the last element from the list
numbers.sort()  # ascending order
numbers.reverse()  # descending order

# behavior of the members of list
print(numbers.index(5))  # .index(x) returns the index of x
print(50 in numbers)  # returns a boolean value
print(numbers.count(5))  # counts how many 5s are there

# copy list (our main list can't be affected)
numbers2 = numbers.copy()
numbers3 = numbers[:]

# print(numbers)
