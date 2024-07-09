# for x in range(4):
#     for y in range(4):
#         print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    # print("x" * x_count)  note: this is an easier solution

    output = ""
    for count in range(x_count):  # we are not using count value, this is for just running iteration
        output = output + "x"
    print(output)
