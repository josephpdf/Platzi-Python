# dia = input("Ingrese un número del 1 al 7 para conocer el día de la semana: ")
# dia = int(dia) # Convertimos el input a un número entero

dia = 4

match dia:
    case 1:
        print("Hoy es Lunes")
    case 2:
        print("Hoy es Martes")
    case 3:
        print("Hoy es Miércoles")
    case 4:
        print("Hoy es Jueves")
    case 5:
        print("Hoy es Viernes")
    case 6:
        print("Hoy es Sábado")
    case 7:
        print("Hoy es Domingo")
    case _:
        print("No coincide con ninguna de las anteriores")