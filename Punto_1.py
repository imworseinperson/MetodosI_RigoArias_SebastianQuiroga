
# PUNTO 1 #

def tuplas_yml(file_path):
    with open(file_path, 'r') as file:
        yml_content = file.read()
        
        # Encontrar el inicio y fin de la sección de datos
        start_index = yml_content.find("data: | -")
        end_index = yml_content.find("\n\n", start_index)
        data_section = yml_content[start_index:end_index].strip()

        # Extraer las tuplas (λi, ni) del texto
        data_tuples = []
        
        data_lines = data_section.split("\n| -")
        for line in data_lines[1:]:  # Saltar el primer elemento en blanco
            parts = line.strip().split()
            if len(parts) == 2:
                wavelength = float(parts[0])
                refractive_index = float(parts[1])
                data_tuples.append((wavelength, refractive_index))
        
        return data_tuples


yml_file = r'C:\Users\rigod\OneDrive\Escritorio\Metodos Grupo\MetodosI_RigoArias_SebastianQuiroga\Adhesivos Ópticos'
data_tuples = tuplas_yml(yml_file)
print(data_tuples)











