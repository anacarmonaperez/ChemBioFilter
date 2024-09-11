import sys

if len(sys.argv) != 3:  # Se esperan 2 argumentos: fichero_CoMentoriginal, CTD_extraido_u
    print("Uso: match_coincidencias.py CoMentoriginal CTD_extraido_u", file=sys.stderr)
    exit()

# Definir los argumentos
coment_original = sys.argv[1]  # Archivo CoMent original
CTD_extraido = sys.argv[2]  # Archivo CTD extraído

# Listas para almacenar las coincidencias
coment = []
match = []

def leer_dos_columnas(filename):
    xcoment = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                l_line = line.strip().split("\t")
                key_coment = f"{l_line[0]}\t{l_line[1]}"  # Concatenar Mesh y GO como clave
                xcoment[key_coment] = True  # No es necesario almacenar el valor, solo la clave
                coment.append(key_coment)  # Añadir a la lista de coincidencias
        return xcoment
    except:
        print("Error: file not found", file=sys.stderr)
        exit()

def leer_dos_columnas_lista(filename):
    data = []
    try:
        with open(filename, "r") as f:
            for line in f:
                l_line = line.strip().split("\t")
                data.append(f"{l_line[0]}\t{l_line[1]}")  # Concatenar Mesh y GO
        return data
    except:
        print("Error: file not found", file=sys.stderr)
        exit()

data_coment = leer_dos_columnas(coment_original)
data_CTD = leer_dos_columnas_lista(CTD_extraido)

# Crear y escribir el archivo de coincidencias
with open("match_final.txt", "w") as match_final:
    for key_CTD in data_CTD:
        if key_CTD in data_coment:
            match_final.write(f"{key_CTD}\n")
            match.append(key_CTD)

# Imprimir el número de coincidencias encontradas (opcional para diagnóstico)
print(f"Número de coincidencias encontradas: {len(match)}")
