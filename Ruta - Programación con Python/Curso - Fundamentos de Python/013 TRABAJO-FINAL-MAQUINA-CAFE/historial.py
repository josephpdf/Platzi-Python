ARCHIVO_PEDIDOS = "pedidos.txt"

def ver_historial():
    try:
        print("\nHistorial de pedidos")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines() # Lee todas las líneas del archivo y las almacena en una lista llamada pedidos
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1): # enumerate nos permite obtener el índice de cada pedido, comenzando desde 1
                    print(str(i) + ". " + pedido.strip()) # Imprime el número del pedido seguido del nombre del café, utilizando strip() para eliminar cualquier espacio en blanco adicional
            else:
                print("Aún no hay ningún pedido")
    except FileNotFoundError:
        print("\nTodavía no existe un historial de pedidos")