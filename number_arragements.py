# Input del ususario
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

# Calcula producto y suma
product = num1 * num2
sum = num1 + num2

# organiza los números de mayor a menor
numbers = [num1, num2, product, sum]
numbers.sort(reverse=True)

# output de los números organizados
print("Arranged numbers from biggest to smallest:")
for number in numbers:
    print(number)