import math

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

square_roots = [math.sqrt(num) for num in range(start, end + 1)]

even_values = [val for val in square_roots if int(val) % 2 == 0]
odd_values = [val for val in square_roots if int(val) % 2 != 0]

print("\nSquare roots:", square_roots)
print("Even values:", even_values)
print("Odd values:", odd_values)