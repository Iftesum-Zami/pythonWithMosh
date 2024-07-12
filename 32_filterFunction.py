# .filter() is a built in function
# something.filter(function, iterable):
# returns an item from iterable under True condition, skips the False

def find_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


x = [552, 641, 891, 122, 453, 228]
# y = []
# for number in x:
#     if find_even(number):
#         y.append(x[])  # didn't find what to do
# --- above ? lines code are equivalent to following 1 line code ---

y = list(filter(find_even, x))  # filter(find_even, x) is a filter object, we have to convert it to list

print(y)
