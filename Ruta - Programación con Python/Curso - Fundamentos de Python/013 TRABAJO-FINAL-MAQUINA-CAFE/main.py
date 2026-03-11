from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:
        # Mostrar el menú de opciones
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Pedir un cafe
            pedir_cafe()
        elif opcion == "2":
            # Ver el historial
            ver_historial()
        elif opcion == "3":
            print("\nMuchas gracias por haber tomado nuestro café, vuelva pronto! \n")
            break
        else:
            print("\nOpción inválida, por favor indique una de las opciones sugeridas \n")

if __name__ == "__main__": # Esto asegura que el código dentro de este bloque solo se ejecute si el archivo se ejecuta directamente, no si se importa como módulo.
    main()