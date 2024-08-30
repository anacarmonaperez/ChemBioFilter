import sys
import networkx as nx
import obonet
#Esta biblioteca proporciona métodos para convertir objetos de Python a cadenas JSON y viceversa:
import json
if len(sys.argv) != 2:
	print("python3 go-basic3.py go-basic.obo")
	sys.exit(1)
filename=sys.argv[1]


try:
	graph = obonet.read_obo(filename, ignore_obsoletes = True) #Leer el fichero transformandolo de obo a grafo
	
	print(graph)

except FileNotFoundError:
    print(f"Error: El archivo {filename} no se encontró.")
    sys.exit(1)

#Definir variables
is_a = 'is_a'
part_of = 'part_of'

#Crear lista de aristas del grafo para eliminar que no son is_a ni part_of
edges_to_del=[]

#Crear lista para obtener los nodos del grafo, con un bucle para cada nodo de esta lista
for node in graph.nodes():
	#print(node)

	#nodo desde el que proviene la arista, nodo hacia cual va la arista y clave de la arista/ devuelve una lista de tuplas que representan todas las aristas entrantes al nodo especificado.
	for parent, child, key in graph.in_edges(node, keys=True):
	
		#si la condicion no se cumple se añade a la lista para borrar 
		if (key != part_of) and (key != is_a):
			edges_to_del.append((node,child))
			print(f'• {child} ⟵ {key} ⟵ {parent}')
			
#eliminar lista con el resto de aristas
graph.remove_edges_from(edges_to_del)
#print(graph)


#Crear diccionario de los tres nodos principales en una variable 
variable={}

#Definir valores de los tres nodos principales
head_of_GO= { "biological_process" : "GO:0008150",
	"molecular_function" : "GO:0003674",
	"cellular_component" : "GO:0005575"
}


#Para cada nodo del grafo
for node in graph.nodes():
	#Tipo de nodo
	node_type=graph.nodes[node]["namespace"]
	
	#Entonces mide la distancia del grafo entre los nodos hasta los nodos principales, -1 sin tener en cuenta el primero
	dist = len(nx.shortest_path(graph,node,target=head_of_GO[node_type])) -1 
		
	# Inicializar variable[node] como un diccionario vacio si no existe
	#Si no haces la verificación e inicialización, Python no sabe cómo manejar la clave node en variable, resultando en el KeyError
	if node not in variable:
		variable[node] = {}
		
  	#Añadir al diccionario variable el tipo de nodo con sus distancias correspondientes
	variable[node]["distance"] = dist
	variable[node]["namespace"] = node_type

#print(variable)

#Convertir diccionario en lista de tuplas
variable_list = [(node, data["distance"], data["namespace"]) for node, data in variable.items()]

#Convertir tuplas a cadenas separadas por tabuladores
variable_str = ["\t".join(map(str, item)) for item in variable_list]

# Imprimir las líneas formateadas
output_filename = "output.txt"
with open(output_filename, "w") as output_file:
	for line in variable_str:
    		output_file.write(f"{line}\n")
    		
print(f"El diccionario se ha guardado en {output_filename}")









