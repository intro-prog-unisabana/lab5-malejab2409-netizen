import os

directorio_actual = os.getcwd()
print(f"Current working diectory: {directorio_actual}")

import math
num = input("Enter an integer: ")
resultado = math.log2(int(num))
print(f"Log base 2 of {num} is: {resultado}")

floor = math.floor(resultado)
ceil = math.ceil(resultado)
print(f"Floor: {floor}")
print(f"Ceiling: {ceil}")