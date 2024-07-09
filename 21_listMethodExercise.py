numbers = [1, 5, 6, 5, 1, 2, 3]
uniques = []
duplicate = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print("List without repeating the numbers:", uniques)

# for num in numbers:
#     if numbers.count(num) > 1:
#         duplicate.append(num)
# print(duplicate)

# the above code also works, but it returns the element multiple times.
# To avoid this, we have to recheck if the item is in the duplicate[] list. Just like printing unique list

for num in numbers:
    if numbers.count(num) > 1:  # for selecting the numbers which occur more than 1 time
        if num not in duplicate:  # not for repeating the selected numbers
            duplicate.append(num)
print("The list of duplicate numbers:", duplicate)
