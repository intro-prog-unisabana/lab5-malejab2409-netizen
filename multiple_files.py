from utils import count_letters, flip, greet 

entrada = input ("Please type your message\n")
invertido = flip(entrada)
cantidad = count_letters(entrada)
codificado = f"{invertido}{cantidad}"
print(f"Your encoded message is: {codificado}1 ")