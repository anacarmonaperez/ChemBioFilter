import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if len(sys.argv) != 5 and len(sys.argv) != 4: #si no tiene 4 argumentos da error
	print("Uso: match_vdiccplot_comorig.py  fichero_CoMentoriginal  CTD_extraido_u  columna_datos  [opcion_n]", file=sys.stderr)
	exit()

#definir cada argumento	
coment_original = sys.argv[1] #4 col
CTD_extraido = sys.argv[2]
columna_datos = int(sys.argv[3])

# Comprobar si opcion_n se ha proporcionado (solo se necesita para la columna 4)
if len(sys.argv) == 5:
    opcion_n = sys.argv[4]
else:
    opcion_n = None


#diccionario para los plots
columnas={
	2 : "articulos_mesh",
	3 : "articulos_GO",
	4 : "n",
	5 : "p_valor"
	}

#condicional si las columnas  estan en las columnas de coment original (datos)
if columna_datos in columnas:
	tag = columnas[columna_datos]
else:
	print("Error", columnas)
	#quit()

# Validación de la opción para "n"
if columna_datos == 4 and opcion_n not in ["normal", "min"]:
    print("Error: Opción para 'n' debe ser 'normal' o 'min'.", file=sys.stderr)
    exit()

# Actualizar el tag para "nmin" si se selecciona la opción "min"
if columna_datos == 4:
    if opcion_n == "min":
        tag = "nmin"
    elif opcion_n == "normal":
        tag = "n"
elif columna_datos == 5:
		opcion_n = None  # No se necesita opcion_n para la columna 5


#2 listas para los plots (2 pval, 2 n)
coment=[]
match=[]
#exit()

def leer_dos_columnas(filename): #definir funcion de diccionario
	xcoment={}
	#almacene las lineas
	try:
			
		with open(filename,"r") as f:#ABRIR Y LEER ARCHIVO
				
			for line in f: #definir valores y claves del diccionario y variable local: coment
				l_line=line.strip().split("\t") #pasar de cadena a lista
				key_coment = f"{l_line[0]}\t{l_line[1]}"
				if columna_datos == 4:  # Si la columna es "n"
					if opcion_n == "normal":
						value_coment = float(l_line[columna_datos])
					elif opcion_n == "min":
						value_coment = float(l_line[columna_datos])/min(float(l_line[2]), float(l_line[3]))
				else:
					value_coment = float(l_line[columna_datos])

				if value_coment > 0:  # Filtrar valores no positivos
					xcoment[key_coment] = value_coment
					coment.append(value_coment)
			
		return xcoment #devolver resultado de la funcion
	except:
		print("error: file not found coment", file=sys.stderr)
#exit()	

def leer_dos_columnas_lista(filename): #definir funcion de lista
	data=[] #almacene las lineas
	try:
			
		with open(filename,"r") as f:#ABRIR Y LEER ARCHIVO
				
			for line in f:
				l_line=line.strip().split("\t") #pasar de cadena a lista
				
				data.append(l_line) #almacenar en la lista
		return data #devolver resultado de la funcion
	except:
		print("error: file not found ctd", file=sys.stderr)

#exit()

data_coment= leer_dos_columnas(coment_original) #funcion referida al diccionario
data_CTD= leer_dos_columnas_lista(CTD_extraido) #funcion referida a la lista


for line_CTD in data_CTD: #para cada linea de CTD en la lista de CTD
		#	print(line_CTD)
	mesh_CTD = line_CTD[0]    #defino la clave de CTD como diccionario porque lo tengo que meter con clave de diccionario para compararlo con el diccionario coment
	GO_CTD = line_CTD[1]
	key_CTD = f"{mesh_CTD}\t{GO_CTD}"

	if key_CTD in data_coment: #si la clave CTD esta en el diccionario de coment
		match.append(data_coment[key_CTD])






# Filtrar valores válidos para log10 y evitar valores no positivos
def filter_for_log(values):
    return [x for x in values if x > 0]

# Aplicar el filtro a las listas antes de aplicar np.log10
filtered_coment = filter_for_log(coment)
filtered_match = filter_for_log(match)

# Verificar si las listas filtradas están vacías (lo que significaría que todos los valores fueron cero o negativos)
if not filtered_coment or not filtered_match:
    print("Error: Todos los valores son cero o negativos, no se puede calcular el logaritmo.", file=sys.stderr)
    exit()



#sns plot 1
plt.figure()
plt.title("Distribucion_log_" + tag)
plt.xlabel(tag)
sns.kdeplot(np.log10(coment),label="Coment")
sns.kdeplot(np.log10(match),label="Match")
plt.legend()
plt.savefig("analisis_log_" + tag + ".jpg")
plt.close()

#sns plot 2
plt.figure()
plt.title("Distribucion_" + tag)
plt.xlabel(tag)
sns.kdeplot(coment,label="Coment")
sns.kdeplot(match,label="Match")
plt.legend()
plt.savefig("analisis_" + tag + ".jpg")

