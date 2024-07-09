numbers = [1, 5, 6, 5, 1, 2, 3]
duplicate = []
for num in numbers:
    if numbers.count(num) > 1:
        if num not in duplicate:
            duplicate.append(num)
print("The list of duplicate numbers:", duplicate)
