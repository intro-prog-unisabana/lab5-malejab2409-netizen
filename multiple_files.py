from utils import flip, count_letters

entrada = input("Please type your message\n")
invertido = flip(entrada)
cantidad_a = count_letters(entrada)
codificado = f"{invertido}{cantidad_a}"
print(f"Your encoded message is: {codificado}")