import matplotlib.pyplot as plt
import numpy as np
import os
import yaml

# PUNTO 1 #

def tuplas_yml(file_path):
    
    with open(file_path, 'r') as file:
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



data_tuples = tuplas_yml(r"C:\Users\rigod\Documents\Metodos Grupo\MetodosI_RigoArias_SebastianQuiroga\Adhesivos Ópticos\NOA1348.yml")


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
    
print(refractive_index_graph(data_tuples, 'NOA1348'))


def t_files(file_path):

    lista_archivos = os.listdir(file_path)
    lista_tuplas = []
    for archivo in lista_archivos:
        with open(os.path.join(file_path, archivo), "r") as f:
            datos = yaml.safe_load(f)
            if "data: |" in datos and "SPECS" in datos:
                lista_tuplas.append(datos)
    return lista_tuplas

def crear_graficas(data_tuples):
    for tupla in data_tuples:
        refractive_index_graph(tupla)

def main(file_path):

    directorio = file_path
    lista_tuplas = t_files(directorio)
    crear_graficas(lista_tuplas)

print(main(r"C:\Users\rigod\OneDrive\Escritorio\MetodosI_RigoArias_SebastianQuiroga-1\Adhesivos Ópticos\NOA1348.yml"))







# PUNTO 2 #








