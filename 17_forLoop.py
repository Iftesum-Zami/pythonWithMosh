# for item in 'Python':
#     print(item)
# print("This is out of loop !")

names = ["Mosh", "John", "Sarah"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
rangeOfNumbers = range(1, 10, 2)  # range(first{including}, last{excluding}, increment/decrement)

for item in rangeOfNumbers:
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total = total + price
print(f"Total price: {total}")
