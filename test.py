score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score <= 89:
    print("Your grade is B")
elif 70 <= score <= 79:
    print("Your grade is C")
elif 60 <= score <= 69:
    print("Your grade is D")
elif 50 <= score <= 59:
    print("Your grade is E")
elif 40 <= score <= 49:
    print("Your grade is E-")
elif score < 40:
    print("Your grade is F or Fail")
else:
    print("Invalid Input")
