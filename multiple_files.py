from utils import flip, count_letters

mensaje = input("Please type your message\n")

invertido = flip(mensaje)
cantidad_a = count_letters(mensaje, 'a')
codificado = f"{invertido}{cantidad_a}"


print(f"Your encoded message is: {codificado}")