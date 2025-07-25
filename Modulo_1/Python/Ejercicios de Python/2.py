cesta = []
seguir = True

while seguir:
    print("1. Agregar producto")
    print("2. Mostrar cesta")
    print("3. Eliminar producto")
    print("4. Calcular total")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cesta.append([nombre, precio])
        print(f'{nombre} agregado a la cesta.') 
    elif opcion == "2":
        if cesta:
            print("Contenido de la cesta:")
            for item in cesta: 
                nombre, precio = item
                print(f"{nombre} = {precio}")
        else:
            print("La cesta está vacía.")
    elif opcion == "3":
        nombre = input("Nombre del producto a eliminar: ")
        for item in cesta:
            if item[0] == nombre:
                cesta.remove(item)
                print(f'{nombre} eliminado de la cesta.')
                break
        else:
            print(f'{nombre} no se encuentra en la cesta.')
    elif opcion == "4":
        total = sum(item[1] for item in cesta)
        print(f'Total de la compra: {total}')
    elif opcion == "5":
        print("Hasta luego bro, te esperamos cuando quieras volver")
        seguir = False