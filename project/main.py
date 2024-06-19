from Operaciones import *
while (True):
    print("1) Crear lista de productos\n2) Salir")
    op=int(input("Ingresa una opcion:\n"))
    if op==1:
        insertarProducto()
        showPr()
    elif op==2:
        break