#Taller 3 - Programacion
# Benjamin Hidalgo - Leandro Sepúlveda - Franco Perez

import numpy as np

listaNombres = [] #NombreProducto
listaPrecios = [] #PrecioUnitario
listaStocksAlmacenFerreteria = [] #StockAlmacenFerreteria
listaCategorias = [] #,Categoria
listaProveedores = [] #Proveedor

#MAIN

def lecturaArchivo():
    
    with open("ferreteria.txt", "r") as archivo:
        linea = archivo.readline().strip()
        while linea != "":
            partes = linea.split(",")
            nombre = partes[0]
            precio = float(partes[1])
            stockAlmacen = int(partes[2])
            stockFerreteria = int(partes[3]) 
            categoria = partes[4]
            proveedor = partes[5]
        
            listaNombres.append(nombre)
            listaPrecios.append(precio)
            listaStocksAlmacenFerreteria.append(((stockAlmacen, stockFerreteria, nombre)))
            listaCategorias.append(categoria)
            listaProveedores.append(proveedor)

            linea = archivo.readline().strip()
        
        archivo.close()

columnas = len(listaNombres)
filas = 2
stocksM = np.zeros(filas, columnas)

for stockAlmacen, stockFerreteria, nombre in listaStocksAlmacenFerreteria:
    if nombre in listaNombres:
        j = listaNombres.index(nombre)
        stocksM[0][j] = stockAlmacen
        stocksM[1][j] = stockFerreteria
