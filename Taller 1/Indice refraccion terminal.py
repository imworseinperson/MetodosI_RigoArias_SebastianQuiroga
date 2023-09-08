## Indice refraccion terminal

import os
import csv
import requests

# Descarga y guarda los darchivos yml en carpetas segun el nombre de la categoria dentro de una carpeta que se llama archivos_yml #

archivos_yml_dir = os.path.join(os.getcwd(), 'archivos_yml')

# Lee el archivo CSV
with open('indices_refraccion.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Saltar la primera línea de encabezados
    for row in csv_reader:
        category = row[0]
        material_name = row[2]
        yaml_url = row[3]

        # Crea la carpeta de la categoría si no existe
        if not os.path.exists(archivos_yml_dir):
            os.makedirs(archivos_yml_dir)

        # Crea la carpeta de la categoría en la carpeta "archivos_yml"
        category_dir = os.path.join(archivos_yml_dir, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        # Descarga el archivo .yml y lo guarda en la carpeta adecuada
        response = requests.get(yaml_url)
        yml_file_path = os.path.join(archivos_yml_dir, category, f'{material_name}.yml')
        with open(yml_file_path, 'wb') as yml_file:
            yml_file.write(response.content)

# Crea la carpeta materiles.txt con la lista de los nombres de los materiales

# Import-Csv indices_refraccion.csv | Select-Object -ExpandProperty Material | Out-File -FilePath materiales.txt
