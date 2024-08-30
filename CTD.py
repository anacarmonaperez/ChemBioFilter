import sys
if len(sys.argv) != 2:
	print("python3 CTD.py CTDsin.tsv")
	exit()
filename=sys.argv[1]
	
#Abrir archivo en modo lectura
try:
	f1_in = open (filename,"r")
	print("f1_in",file=sys.stderr)
except:
	print("error")

# Lista donde se guardarán las duplas que hagan match
matches = []


# Abre el archivo de salida en modo escritura
with open("CTD_extraido.txt", "w") as f_out:
	for line in f1_in:
		# Paso de lista a cadena separada por tabulaciones con salto de linea
		l_line=line.strip().split("\t")

		# Extraer las columnas 1 (índice 0) y 4 (índice 3)
		columna_2 = l_line[1]
		columna_5 = l_line[4]
		# print("\t".join([l_line[i] for i in [1,4]]))

		# Escribir en el archivo de salida
		f_out.write(f"{columna_2}\t{columna_5}\n")

# Cerrar el archivo de entrada
f1_in.close()
	
print("Proceso completado. Columnas 2 y 5 extraídas en CTD_extraido.txt")
	

