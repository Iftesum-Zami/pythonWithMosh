# .map() is a built in function
# something.map(function, iterable)
# returns an iterator that applies function to every item of iterable

def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num


x = [552, 641, 891, 122, 453, 228]
# y = []
# for number in x:
#     y.append(make_even(number))
# --- above 3 line code is equivalent to following 1 line code ---

y = list(map(make_even, x))  # map(make_even, x) is a map object, we have to convert it to list

print(y)
