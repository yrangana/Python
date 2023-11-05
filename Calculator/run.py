number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

# Add two numbers
sum = float(number1) + float(number2)

# Display the sum
# will print value as float
print("The sum of {0} and {1} is {2}".format(number1, number2, sum))

# will print value as integer
print("The sum of {0} and {1} is {2}".format(number1, number2, int(sum)))

# will print value as string
print("The sum of {0} and {1} is {2}".format(number1, number2, str(sum)))
