def list_shift (lista, cantidad ):
    for i in range(len(lista)):
        lista[i] = lista [i] + cantidad
def calc_avg (lista):
    return sum(lista) / len(lista)
def print_normalized (lista):
    print(lista)
valores = [2.0, 4.0, 6.0, 8.0]
prom = calc_avg(valores)
list_shift(valores, -prom)
print_normalized(valores)