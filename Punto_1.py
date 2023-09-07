import matplotlib.pyplot as plt
import numpy as np
import os
import chardet

# PUNTO 1 #

def tuplas_yml(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        yml_content = file.read()
        
        # Encontrar el inicio y fin de la sección de datos
        start_index = yml_content.find("data: |")
        end_index = yml_content.find("SPECS", start_index)
        data_section = yml_content[start_index:end_index].strip()
        

        # Extraer las tuplas (λi, ni) del texto
        data_tuples = []
        
        data_lines = data_section.split("\n")
        
        for line in data_lines[1:]:  # Saltar el primer elemento en blanco
            parts = line.strip().split()
            parts_list = list(parts)
            
            if len(parts) == 2:
                
                wavelength = float(parts_list[0])
                refractive_index = float(parts_list[1])
                data_tuples.append((wavelength, refractive_index))
                
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

    archivos = []
    for root, directories, files in os.walk(carpeta):
        for archivo in files:
            if os.path.isfile(os.path.join(root, archivo)):
                archivos.append(archivo)
    return archivos


archivos = files_names(r"C:\Users\rigod\Documents\MetodosI_RigoArias_SebastianQuiroga\archivos_yml")

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
    files = files_names(file_path)
    for root, directories, files in os.walk(file_path):
        # Procesar cada archivo
        for file in files:
            
            # Obtener los datos del archivo
            data_tuples = tuplas_yml(os.path.join(root, file))

            # Guardar la gráfica
            save_graph(data_tuples, file, root)

main(r"C:\Users\rigod\Documents\MetodosI_RigoArias_SebastianQuiroga\archivos_yml")

# PUNTO 2 #








