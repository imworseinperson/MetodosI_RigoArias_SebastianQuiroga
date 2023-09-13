import matplotlib.pyplot as plt
import numpy as np
import os
import chardet

# PUNTO 1 #

def tuplas_yml(ruta_yml: str) -> list:
    '''
    Lee los archivos yml y devuelve la lista de tuplas
    '''
    f = open(ruta_yml)
    texto_archivo = f.read() #text_archivo es un string de todo lo que contiene el archivo
    f.close()

    lista_unprocessed = texto_archivo.split('data: |\n')[1].split('\nSPECS')[0].split('  - type')[0].strip().split('\n        ')
    
    data_tuples = []
    

    for k in lista_unprocessed:
        texto = k.split(' ')
        texto[0] = float(texto[0])
        texto[1] = float(texto[1])
        data_tuples.append(tuple(texto))

    return data_tuples


def mean(data_tuples):
    
    first_values = [ ]
    
    for tuple in data_tuples:
        
        first_values.append(tuple[1])
        
    return sum(first_values) / len(first_values)


def s_deviation(data_tuples):
    
    first_values = []
    
    for tuple in data_tuples:
        
        first_values.append(tuple[0])
        mean = sum(first_values) / len(first_values)
        squared_differences = [(x - mean)**2 for x in first_values]
        variance = sum(squared_differences) / (len(first_values))
        
    return np.sqrt(variance)


def refractive_index_graph(data_tuples, material):
    
    wavelength = [tupla[0] for tupla in data_tuples]
    refractive_index = [tupla[1] for tupla in data_tuples]
    refractive_index_mean = mean(data_tuples)
    refractive_index_s_deviation  = s_deviation(data_tuples)
    plt.figure(figsize=(10, 8))

    plt.title(f"Indice de refraccion de {material}, n promedio = {refractive_index_mean}, desviacion estandar = {refractive_index_s_deviation} ")

    plt.xlabel("Longitud de onda (nm)")
    plt.ylabel("Índice de refracción")

    plt.plot(wavelength, refractive_index)

    plt.grid(True)

    plt.show()
    


def files_names(carpeta):

    names = []
    for root, directories, files in os.walk(carpeta):
        for archivo in files:
            if os.path.isfile(os.path.join(root, archivo)):
                names.append(archivo)
    return names

def save_graph(data_tuples, material, dir_path):
    
    wavelength = [tupla[0] for tupla in data_tuples]
    refractive_index = [tupla[1] for tupla in data_tuples]
    refractive_index_mean = mean(data_tuples)
    refractive_index_s_deviation = s_deviation(data_tuples)

    plt.figure(figsize=(10, 8))

    plt.title(f"Índice de refracción de {material}, n promedio = {refractive_index_mean}, desviación estándar = {refractive_index_s_deviation}")

    plt.xlabel("Longitud de onda (nm)")
    plt.ylabel("Índice de refracción")

    plt.plot(wavelength, refractive_index)

    plt.grid(True)

    plt.savefig(os.path.join(dir_path, f"{material}.png"))

def main(file_path):
    
    # Obtener la lista de archivos

    
    for root, directories, files in os.walk(file_path):
            # Procesar cada archivo
        for file in files:
                
            # Obtener los datos del archivo
            data_tuples = tuplas_yml(os.path.join(root, file))

            # Guardar la gráfica
            save_graph(data_tuples, file, root)

main(r"C:\Users\rigod\Documents\MetodosI_RigoArias_SebastianQuiroga\archivos_yml\Materia Orgánica")

# Para el punto 1 no logre hacer que iterara, sin embargo, considero importante mencionar mi analisis. Basicamente cree la
# funcion files_names para tener una lista con los nombres de cada archivo .yml, esto para luego usarlo como variable en la 
# funcion main() haciendo que itere por estos archivos, cambiando el nombre de ruta, sin embargo, no puude entrar en cada carpeta 
# para luego llamar el archivo, ahi falle :(. Igual realmente sabia que hacer, era solo para comentar xd. bai, exitos!

# PUNTO 2 #








