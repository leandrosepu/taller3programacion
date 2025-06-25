# Taller 3 - Programación
# Benjamin Hidalgo - Leandro Sepúlveda - Franco Perez

import numpy as np
import time
import random

listaNombres = []  # NombreProducto
listaPrecios = []  # PrecioUnitario
listaStocksAlmacenFerreteria = []  # (StockAlmacen, StockFerreteria, Nombre)
listaCategorias = []  # Categoria
listaProveedores = []  # Proveedor

# FUNCIÓN PARA LEER DATOS DESDE ARCHIVO
def lecturaArchivo():
    with open("ferreteria.txt", "r") as archivo:
        linea = archivo.readline().strip()
        while linea != "":
            partes = linea.split(",")
            nombre = partes[0].lower()
            precio = float(partes[1])
            stockAlmacen = int(partes[2])
            stockFerreteria = int(partes[3])
            categoria = partes[4].lower()
            proveedor = partes[5]

            listaNombres.append(nombre)
            listaPrecios.append(precio)
            listaStocksAlmacenFerreteria.append((stockAlmacen, stockFerreteria, nombre))
            listaCategorias.append(categoria)
            listaProveedores.append(proveedor)

            linea = archivo.readline().strip()
        archivo.close()

# FUNCIÓN PARA LLENAR MATRIZ DE STOCKS
def llenarValores():
    columnas = len(listaNombres)
    filas = 2
    stocksM = np.zeros((filas, columnas))
    for stockAlmacen, stockFerreteria, nombre in listaStocksAlmacenFerreteria:
        if nombre in listaNombres:
            j = listaNombres.index(nombre)
            stocksM[0][j] = stockAlmacen
            stocksM[1][j] = stockFerreteria

# FUNCIÓN PARA GENERAR CÓDIGOS ÚNICOS
def generarCodigosUnicos():
    cantidad = len(listaNombres)
    codigos = random.sample(range(10000, 100000), cantidad)  # Códigos de 5 dígitos únicos
    return codigos

# EJECUCIÓN INICIAL
lecturaArchivo()
llenarValores()
listaCodigos = generarCodigosUnicos()

# MENÚ PRINCIPAL
def menuPrincipal():
    while True:
        print("\n***** MENÚ *****")
        time.sleep(1)
        print("[1]. Buscar producto")
        print("[2]. Agregar/Borrar productos")  # aún no implementado
        print("[3]. Ver todos los productos")
        print("[0]. Salir")

        opc = input("Ingresa una opción: ")

        if opc == "1":
            print("\n📌 Buscar producto por:")
            print("[1] Código")
            print("[2] Nombre")
            subopc = input("Elige una opción: ").strip()

            if subopc == "1":
                codigoBuscar = input("Ingresa el CÓDIGO del producto (5 dígitos): ").strip()
                if not codigoBuscar.isdigit() or len(codigoBuscar) != 5:
                    print("❌ Código inválido. Debe ser un número de 5 dígitos.")
                    continue

                encontrado = False
                for i in range(len(listaCodigos)):
                    if str(listaCodigos[i]) == codigoBuscar:
                        print("\n✅ Producto encontrado:")
                        print("----------------------------")
                        print(f"Código       : {listaCodigos[i]}")
                        print(f"Nombre       : {listaNombres[i].capitalize()}")
                        print(f"Precio       : ${listaPrecios[i]:,.0f}")
                        print(f"Stock Almacén: {listaStocksAlmacenFerreteria[i][0]}")
                        print(f"Stock Local  : {listaStocksAlmacenFerreteria[i][1]}")
                        print(f"Categoría    : {listaCategorias[i].capitalize()}")
                        print(f"Proveedor    : {listaProveedores[i]}")
                        print("----------------------------")
                        encontrado = True
                        break

                if not encontrado:
                    print("❌ No se encontró ningún producto con ese código.")

            elif subopc == "2":
                nombreBuscar = input("Ingresa el NOMBRE del producto: ").strip().lower()
                encontrados = []

                for i in range(len(listaNombres)):
                    if nombreBuscar in listaNombres[i]:
                        encontrados.append(i)

                if len(encontrados) == 0:
                    print("❌ Producto no encontrado.")
                else:
                    for i in encontrados:
                        print("\n✅ Producto encontrado:")
                        print("----------------------------")
                        print(f"Código       : {listaCodigos[i]}")
                        print(f"Nombre       : {listaNombres[i].capitalize()}")
                        print(f"Precio       : ${listaPrecios[i]:,.0f}")
                        print(f"Stock Almacén: {listaStocksAlmacenFerreteria[i][0]}")
                        print(f"Stock Local  : {listaStocksAlmacenFerreteria[i][1]}")
                        print(f"Categoría    : {listaCategorias[i].capitalize()}")
                        print(f"Proveedor    : {listaProveedores[i]}")
                        print("----------------------------")

            else:
                print("❌ Opción no válida.")

        elif opc == "2":
            print("🔧 Funcionalidad de agregar/borrar productos en construcción...")

        elif opc == "3":
            print("\n📦 Todos los productos:")
            print("-------------------------------------------------------------")
            for i in range(len(listaNombres)):
                print(f"{listaCodigos[i]} - {listaNombres[i].capitalize()} (${listaPrecios[i]:,.0f}) | Almacén: {listaStocksAlmacenFerreteria[i][0]} | Local: {listaStocksAlmacenFerreteria[i][1]}")
            print("-------------------------------------------------------------")

        elif opc == "0":
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")

# INICIO DEL PROGRAMA
menuPrincipal() CHAO LINDO
