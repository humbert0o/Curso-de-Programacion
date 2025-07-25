print("¡BIENVENIDO AL GIMNASIO MACHETE POWER!")

print("Acabas de entrar al gimnasio. Ves dos áreas disponibles:")
print("1.Zona de pesas")
print("2.Zona de cardio")
eleccion = input("¿A qué zona quieres ir? (pesas o cardio): ").lower()

if eleccion == "pesas":
    print("")
    print("Entras a la zona de pesas. Hay tres máquinas libres:")
    print("1. press banca")
    print("2. sentadillas")
    print("3. peso muerto")
    decision = input("¿Qué ejercicio quieres hacer? (banca, sentadillas o muerto): ").lower()
    
    if decision == "banca":
        print("")
        print("Te acuestas en el banco y quieres levantar tu pr, un gymbro está cerca: ")
        print("1.Pedirle que este pendiente por si se te cae la barra")
        print("2.Ignorarlo")
        opcion = input("¿Qué haces? (ayuda o ignorar): ").lower()
        
        if opcion == "ayuda":
            print("El gymbro te está spoteando. Ya no vas a morir")
            print("Ahora puedes intentar más peso.")
            final = input("¿Subir peso? (si o no): ").lower()
            if final == "si":
                print("¡Logras levantar 10kg más! Nuevo récord personal. Fin del juego.")
            else:
                print("Decides ser prudente y terminar tu rutina sin arriesgarte al pr, gg.")
        else:
            print("El gymbro se ofende. Te mira mal todo el entreno. Mal ambiente.")
    
    elif decision == "sentadillas":
        print("Empiezas con sentadillas. Es dia de pierna. Sientes un crujido en la rodilla:")
        print("1.Parar")
        print("2.Continuar")
        print("3.Cambiar a peso liviano")
        opcion = input("Qué haces? (parar, continuar o liviano): ").lower()
        
        if opcion == "parar":
            print("Te faltó odio, venia pr. Pero bueno, mejor prevenir lesiones. Descansas el resto del día.")
        elif opcion == "continuar":
            print("")
            print("Sacaste pr, pero te lesionaste. Tendrás que hacer reposo 2 semanas. Fin del juego.")
        else:
            print("Bajas el peso y completas tu rutina sin problemas. GG.")
    
    else:  
        print("Preparas el peso muerto. Un entrenador te observa:")
        print("1.Demostrar tu fuerza")
        print("2.Pedir que te corrija")
        opcion = input("¿Qué haces? (demostrar o corregir): ").lower()
        
        if opcion == "demostrar":
            print("")
            print("Levantas con mala forma pero logras el peso, cuidado con una lesión.")
        else:
            print("El entrenador mejora tu técnica, ahora realizas el ejercicio perfectamente.")

elif eleccion == "cardio":
    print("Te diriges a las cintas. Hay dos disponibles:")
    print("1. corre a 10km/h")
    print("2. camina en inclinación")
    decision = input("¿Qué eliges? (correr o caminar): ").lower()
    
    if decision == "correr":
        print("A los 5 minutos te duele el costado, agarraste un aire.")
        print("1. bajar velocidad")
        print("2. aguantar el dolor")
        print("3. parar completamente")
        opcion = input("¿Qué haces? (bajar, aguantar o parar): ").lower()
        
        if opcion == "bajar":
            print("Encuentras tu ritmo ideal. Terminaste 5km satisfecho.")
        elif opcion == "aguantar":
            print("Te dió un yeyo, no desayunaste. Terminas en enfermería.")
        else:
            print("Descansas y pruebas otro ejercicio más tarde.")
    
    else:  
        print("Caminas tranquilamente. Oyes una conversación interesante:")
        print("1. acercarte")
        print("2. poner audífonos")
        opcion = input("¿Qué haces? (acercarse o audifonos): ").lower()
        
        if opcion == "acercarse":
            print("Haces un nuevo gymbro.")
        else:
            print("Te concentras en tu música y entreno. Sesión productiva pero solitaria.")

else:
    print("No existe esa zona. El recepcionista te redirige a la entrada.")


print("FIN DE TU ENTRENAMIENTO")
