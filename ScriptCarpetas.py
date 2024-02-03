import os
from os import path as p
import shutil

def buscarCarpetas():
    #obtener carpeta actual
    rutaActual = os.getcwd()
    print(rutaActual)
    #Solicitar segunda carpeta
    carpetaObjetivo = input("Ruta de la carpeta 2")

    # copiar archivos de carpeta 2 a carpeta 1
    for file in os.listdir(carpetaObjetivo):
        print(file)
        shutil.copy("{}//{}" .format(carpetaObjetivo,file),"{}//{}".format(rutaActual,file))
        shutil.SameFileError()

    # copiar archivos de carpeta 2 a carpeta 1    
    for file in os.listdir(rutaActual):
        print(file)
        shutil.copy("{}//{}" .format(rutaActual,file),"{}//{}".format(carpetaObjetivo,file))
        shutil.SameFileError()

buscarCarpetas()