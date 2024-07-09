# list in the list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[0][1])  # first item's 2nd item

for i in matrix: # this is row or individual elements if 1st list
    for j in i:
        print(j)

 