import math

print("Best calculator ever!")

x = int(input("X: "))
y = int(input("Y: "))

print(f"Sum: {x + y}")
print(f"Sub: {x - y}")
print(f"Mul: {x * y}")

if y == 0:
	print("Can't do it!")
else:
	print(f"Div: {x / y}")

print(f"SQRT: {math.sqrt(x)}")