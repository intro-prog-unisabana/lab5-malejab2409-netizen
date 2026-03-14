import random
random.seed(123)
start = int(input("Enter the start value:\n"))
end = int(input("Enter the end value:\n"))


resultado = random.randint(start, end)
print(f"Generates random number:{resultado}")