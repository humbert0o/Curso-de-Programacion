palabra = "banana"
contador = {}

for letra in palabra:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

print(contador)
