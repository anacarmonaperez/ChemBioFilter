# Filtering and Evaluation of Chemical-Biomedical Relationships
Pipeline designed to evaluate and filter the relations between chemical compounds and biomedical terms from literature.

## 1. CTD.py
To use this script, download the CTD file from the CTD database, remove the headers, and save it as "CTDsin.tsv."
This script extracts columns two and five from the file, which contain MeSH and GO identifiers, and saves the output as "CTD_extraido.txt."
```
python3 CTD.py CTDsin.tsv
```
Finally, remove the duplicates from the "CTD_extraido.txt" file and save it as "CTD_extraido_u.txt."

## 2. match_coincidencias.py
To use this script, you need the CTD_extraido_u.txt file and the CoMent_MeshDcomp-GO_2022_s file.
CoMent_MeshDcomp-GO_2022_s file contains MeSH and GO identifiers, number of articles associated with the MeSH term, with the GO term, both terms and p-value.
This script searches for MeSH and GO terms that are common between them and save it as.
```
python3 match_coindicencias.py CoMent_MeshDcomp-GO_2022_s CTD_extraido_u.txt
```

## 3. match_vdiccplot_comorig.py
To use this script, you need the CTD_extraido_u.txt file, the CoMent_MeshDcomp-GO_2022_s file, and specify the column you want to represent in the graphics.
Column five represents the p-value, and column four represents the number of articles.
```
python3 match_vdiccplot_comorig.py CoMent_MeshDcomp-GO_2022_s CTD_extraido_u.txt column_number [option_n]
```
option_n specifies what you want to represent:
- If you want to represent the number of articles, set option_n to "normal."
- If you want to represent the minimum number of articles, set option_n to "min."
- If you want to represent the p-value, leave option_n blank.

## 4. go-basic3.py
To use this script, you need go-basic.obo which you download by GO database.
This script processes an OBO file to build a graph, filters edges, calculates distances from nodes to three main GO terms, and saves the result to "output.txt" file.
```
python3 go-basic3.py go-basic.obo
```

## 5. match_coment_CTDcoment_output.py
To use this scripts, you need CoMent_MeshDcomp-GO_2022_s or CTD_extraido_u.txt and output.txt file
This script reads two input files, matches and updates data from one file with information from the other, and writes the combined results to a new output file.
```
python3 match_coment_CTDcoment_output.py archivo output.txt
```
"Archivo" can be CoMent_MeshDcomp-GO_2022_s or CTD_extraido_u.txt and the results are saved as coment_updated.txt or CTD_updated.txt, respectively.

## 6. match_vdiccplot_comorig_rel.py
To use this script, you need coment_updated.txt CTD_updated.txt and column seven, which is the distances from nodes. 
This script reads two input files containing ontology data, processes and matches the data, and generates histograms to visualize the depth distributions of different ontologies across three categories: "Match," "Coment," and "CTD."
```
python3 match_vdiccplot_comorig_rel.py coment_updated.txt CTD_updated.txt column_number
```
The column is number seven, representing the depth distributions of different ontologies across three categories: "Match," "Coment," and "CTD."























