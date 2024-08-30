import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


if len(sys.argv) != 4: #si no tiene 4 argumentos da error
	print("Uso: mmmm.py  fichero_CoMent_profundiad CTD_extraido_profundiad   columna_datos", file=sys.stderr)
	exit()

#definir cada argumento	
coment_original = sys.argv[1] #4 col
CTD_extraido = sys.argv[2]
columna_datos = int(sys.argv[3])

#diccionario para los plots
columnas={
	2 : "articulos_mesh",
	3 : "articulos_GO",
	4 : "n_min",
	5 : "p_valor",
	7 : "profundidad",
	8 : "namespace"
	}

#condicional si las columnas  estan en las columnas de coment original (datos)
if columna_datos in columnas:
	tag = columnas[columna_datos]
else:
	print("Error", columnas)
	#quit()



#2 listas para los plots 1 y 2 (2 pval, 2 n)
coment=[]
match=[]
#exit()


# Listas para los plots 3 (Coment)
coment_bp = []
coment_cc = []
coment_mf = []

# Listas para los plots 3 (Match)
match_bp = []
match_cc = []
match_mf = []


def leer_dos_columnas(filename): #definir funcion de diccionario
	xcoment={}
	#almacene las lineas
	try:
			
		with open(filename,"r") as f:#ABRIR Y LEER ARCHIVO
			counter = 0
			
		
			for line in f: #definir valores y claves del diccionario y variable local: coment
				l_line=line.strip().split("\t") #pasar de cadena a lista
				key_coment = f"{l_line[0]}\t{l_line[1]}"
				#value_coment= float(f"{l_line[columna_datos]}")
				
				#nuevo value coment para que divida la columna introducida en terminal, es decir, la 4 entre el minimo de la columna dos y tres
				if columna_datos == 4:
					value_coment= float(l_line[columna_datos]) / min(float(l_line[2]), float(l_line[3]))
				
				#otro nuevo value coment para que al extraer la profundidad ([7]) tambien obtenga la columna 8 (tipos de subontologias)
				elif columna_datos == 7:
					value_coment= l_line[columna_datos]+"\t"+ l_line[8]
									
				# y si no que lo ejecute con la columna introducida en la terminal
				else:
					value_coment=float(f"{l_line[columna_datos]}")

				xcoment[key_coment]=value_coment
				#print(line+"\t"+key_coment+"\t"+coment[key_coment]) 
				
				#listas append PLOT 1 Y 2
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
#print(data_coment)
#exit()


output_histograma_match = open("output_histograma_match", "w") #escribir y guardar fichero para convertirlo a df para hacer el histograma
for line_CTD in data_CTD: #para cada linea de CTD en la lista de CTD
	#print(line_CTD)
	mesh_CTD = line_CTD[0]    #defino la clave de CTD como diccionario porque lo tengo que meter con clave de diccionario para compararlo con el diccionario coment        
	GO_CTD = line_CTD[1]
	key_CTD = f"{mesh_CTD}\t{GO_CTD}"
	
	if key_CTD in data_coment: #si la clave CTD esta en el diccionario de coment
		
		output_histograma_match.write(key_CTD+"\t"+ str(data_coment[key_CTD])+"\n") #imprime la clave de CTD que son los comunes más las dos ultimas columnas pero solo las comunes
		#listas append	ctd com
		match.append(data_coment[key_CTD])
		

output_histograma_match.close()	


#DATA FRAMES
#Crear data frame MATCH para representar el histograma para match y coment
df_match = pd.read_csv("output_histograma_match", sep="\t", header=None, names=['GO', 'profundidad', 'subontologia'])
#print(df_match)


#Crear dta frame COMENT / Lee el archivo CSV especificando el delimitador y sin encabezados
df_coment = pd.read_csv("coment_updated.txt", sep="\t", header=None,)
# Selecciona las columnas 1, 7 y 8 del DataFrame
columns_to_select = [1, 7, 8]
df_selected_coment = df_coment.iloc[:, columns_to_select]
df_selected_coment.columns = ['GO', 'profundidad', 'subontologia']

#Crear data frame CTD para representar el histograma para match y coment
df_CTD = pd.read_csv("CTD_updated.txt", sep="\t", header=None, names=['GO', 'profundidad', 'subontologia'])
print(df_CTD)




#FILTRAR PROFUNDIDADES POR SUBONTOLOGIAS PARA HISTOGRAMA
# Filtrar los términos de "biological_process" en match_coment_CTD
df_match_bio = df_match[df_match['subontologia'] == 'biological_process']
df_coment_bio = df_selected_coment[df_selected_coment['subontologia'] == 'biological_process']
df_CTD_bio = df_CTD[df_CTD['subontologia'] == 'biological_process']

# Filtrar los términos de "molecular_function" en match_coment_CTD
df_match_mol = df_match[df_match['subontologia'] == 'molecular_function']
df_coment_mol = df_selected_coment[df_selected_coment['subontologia'] == 'molecular_function']
df_CTD_mol = df_CTD[df_CTD['subontologia'] == 'molecular_function']

# Filtrar los términos de "cellular_component" en match_coment_CTD
df_match_cel = df_match[df_match['subontologia'] == 'cellular_component']
df_coment_cel = df_selected_coment[df_selected_coment['subontologia'] == 'cellular_component']
df_CTD_cel = df_CTD[df_CTD['subontologia'] == 'cellular_component']



#PLOTS
'''	
#exit()
#sns plot 1
ax1=plt.figure()
ax1=plt.title("Distribucion_log_" + tag)
ax1=plt.xlabel(tag)
ax1=sns.kdeplot(np.log10(coment),label="Coment")
ax1=sns.kdeplot(np.log10(match),label="Match")
plt.legend()
plt.savefig("analisis_log_" + tag + ".jpg")
plt.close()

#sns plot 2
ax2=plt.figure()
ax2=plt.title("Distribucion_" + tag)
ax2=plt.xlabel(tag)
ax2=sns.kdeplot(coment,label="Coment")
ax2=sns.kdeplot(match,label="Match")
plt.legend()
plt.savefig("analisis_" + tag + ".jpg")
plt.close()
'''

#sns plot 3 (histogram)
#La opción "stack" apila las distribuciones una sobre otra.
#HISTOGRAMA BP
ax3=plt.hist([df_match_bio['profundidad'], df_coment_bio['profundidad'], df_CTD_bio['profundidad']], bins=range(1, 11), label=["Match", "Coment", "CTD"], alpha=0.7, color=["blue", "orange","green"],
	 density = True)
ax3=plt.xlabel('Profundidad')
ax3=plt.ylabel('Frecuencia')
ax3=plt.title('Histograma Biological Process')
plt.legend()
plt.show()


#HISTOGRAMA MF
ax3=plt.hist([df_match_mol['profundidad'], df_coment_mol['profundidad'], df_CTD_mol['profundidad']], bins=range(1, 11), label=["Match", "Coment","CTD"], alpha=0.7, color=["blue", "orange","green"],
	density = True)
ax3=plt.xlabel('Profundidad')
ax3=plt.ylabel('Frecuencia')
ax3=plt.title('Histograma Molecular Function')
plt.legend()
plt.show()


#HISTOGRAMA CC
ax3=plt.hist([df_match_cel['profundidad'], df_coment_cel['profundidad'], df_CTD_cel['profundidad']], bins=range(1, 11), label=["Match", "Coment","CTD"], alpha=0.7, color=["blue", "orange","green"],
	density = True)
ax3=plt.xlabel('Profundidad')
ax3=plt.ylabel('Frecuencia')
ax3=plt.title('Histograma Cellular Component')
plt.legend()
plt.show()





