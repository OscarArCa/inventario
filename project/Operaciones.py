from Productos import Producto

listaPr = []

def insertarProducto():
    cont = 1
    print("<<<<<<<<<<<<<<<<<<<<<< MENU >>>>>>>>>>>>>>>>>>>")
    while cont <= 10:
        print("""
    1) Ingresar un producto
    2) Salir
                """)
        op = int(input("Ingresa una opcion:\n"))
        if op == 1:
            print("<<<<<<<<<<<<<<<<<<<<<< LLENAR DATOS >>>>>>>>>>>>>>>>>>>")
            id = cont
            nombre = input("Ingresa el nombre:\n")
            precio = float(input("Ingresar precio:\n"))
            Pr = Producto(id, nombre, precio)
            listaPr.append(Pr)
            cont += 1
        elif op == 2:
            break
        else:
            print("¡Esta no es una opción válida!")

def showPr():
    for producto in listaPr:
        print(f"""
        |===================================================|
        ID = {producto.id}
        Nombre = {producto.nombre}
        Precio = {producto.precio}
        SubTotal = {producto.subtotal}
        Precio neto = {producto.precioneto}""")


