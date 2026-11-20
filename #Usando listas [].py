datos = []
cantidad = 1
while True: 
    seleccion = 0
    print("\n", "Productos alimenticios", "1.- Ingresar datos", "2.- Listar los datos", "3.- Buscar un dato", "4.- Salir", sep=("\n") )
    seleccion = int(input("Seleccione acción: "))

    if seleccion == 1:
        while True:
            print("Ingrese nombre del producto [", cantidad , "]")
            producto = input()
            cantidad += 1
            datos.append(producto)
            print("Quiere ingresar otro producto?", "1.- Si", "2.- No", sep=("\n"))
            seleccion = int(input("Seleccione accion: "))
            if seleccion == 2:
                break 
    if seleccion == 2:
        for i in range(len(datos)):
            print(i+1, ".-", datos[i])
    if seleccion == 3:
        bandera = 0
        busqueda = input("Ingrese el producto a buscar: ")
        for i in range(len(datos)):
            if busqueda == datos[i]:
                print("El producto es el numero [" , i+1 ,"]")
                bandera = 1
        if bandera == 0:
            print("Producto no encontrado!")
    if seleccion == 4:
        print("Nos vemos!")
        break                               
