# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the product and sum
product = num1 * num2
sum = num1 + num2

# Arrange the numbers from biggest to smallest
numbers = [num1, num2, product, sum]
numbers.sort(reverse=True)

# Print the arranged numbers
print("Arranged numbers from biggest to smallest:")
for number in numbers:
    print(number)