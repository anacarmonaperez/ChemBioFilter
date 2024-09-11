import sys

if len(sys.argv) != 3:
	print("python3 match_coment_CTDcoment_output.py archivo output.txt") 
	sys.exit()
	
#Definir cada argumento	
archivo = sys.argv[1]
output = sys.argv[2]



def leer_archivo(filename): #definir funcion
	lista=[] #almacene las lineas
	
	try:
		with open(filename,"r") as f: #ABRIR Y LEER ARCHIVO
			for line in f:
				l_line=line.strip().split("\t") #pasar de cadena a lista
			
				lista.append(l_line) #almacenar en la lista
		return lista  #devolver resultado de la funcion

	except:
		print("error: file not found archivo", file=sys.stderr)



#PRIMERO: funcion principal que maneja la lectura, crea diccionario y escribe el nuevo archivo
#SEGUNDO: funcion interna que compara y actualiza los datos

def actualizar_archivos_con_output(archivo, output):
	"""Función para actualizar file1 con información de file2."""

	def actualizar_datos(lista_archivo,lista_output):
		lista_actualizada = []
	#Crear diccionario de output
		output_dict = {}
		for row in lista_output: #para cada fila en la lista de output
    			output_dict[row[0]] = (row[1], row[2]) #clave es la columna terminos go y las columnas distancias y namespaces los valores
    

	# Comparar y añadir datos a archivo
		for row in lista_archivo: #para cada fila en la lista de archivo 
    			if row[1] in output_dict: #si las filas de la columna 2 de archivo estan en el diccionario de output, añade:
        			lista_actualizada.append(row+[output_dict[row[1]][0], output_dict[row[1]][1]])  # Añadir a la columna 2 de archivo (row[1]) la columna 2 ([1]) de output_dict
		print(lista_actualizada)
		return lista_actualizada
		
	#Obtener las listas	
	lista_archivo = leer_archivo(archivo) 
	lista_output = leer_archivo(output)

	#Actualizar los datos
	lista_actualizada2= actualizar_datos(lista_archivo,lista_output)


	# Escribir el resultado del archivo actualizado a un nuevo archivo coment o CTD
	output_filename = "coment_updated.txt"
	with open(output_filename, "w") as f:
   		for row in lista_actualizada2:
        		f.write("\t".join(row) + "\n")
        
	print(f"Archivo {output_filename} creado")


actualizar_archivos_con_output(archivo, output) 
        
        
        
        
        
        
        
        
        
        

