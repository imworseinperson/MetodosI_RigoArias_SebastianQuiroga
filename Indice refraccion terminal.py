## Indice refraccion terminal

import os
import csv
import requests

# Descarga y guarda los darchivos yml en carpetas segun el nombre de la categoria

# Lee el archivo CSV
with open('indices_refraccion.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Saltar la primera línea de encabezados
    for row in csv_reader:
        category = row[0]
        material_name = row[2]
        yaml_url = row[3]

        # Crea la carpeta de la categoría si no existe
        if not os.path.exists(category):
            os.makedirs(category)
        
        # Descarga el archivo .yml y lo guarda en la carpeta adecuada
        response = requests.get(yaml_url)
        yml_file_path = os.path.join(category, f'{material_name}.yml')
        with open(yml_file_path, 'wb') as yml_file:
            yml_file.write(response.content)

# Crea la carpeta materiles.txt con la lista de los nombres de los materiales

# Import-Csv indices_refraccion.csv | Select-Object -ExpandProperty Material | Out-File -FilePath materiales.txt
