# lambda is an anonymous function used to write function in 1 line
# also when function declaration isn't mandatory and we have to pass the function as argument of another function

# def double(x):
#     return x*2
# --------- above 2 lines of code is equivalent to following line -----------

double = lambda x: x*2  # parameter x, return x*2
cube = lambda x: x**3
avg = lambda x, y, z: (x + y + z) / 3

def apply(fx, value):
    6 + fx(value)


print(double(5))
print(cube(2))
print(avg(3, 5, 10))

print(apply(cube, 2))
print(apply(lambda x: x**3, 2))  # this line and previous line has the same functionality
