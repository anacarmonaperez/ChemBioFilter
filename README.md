# Filtering and Evaluation of Chemical-Biomedical Relationships
This pipeline is designed to evaluate and filter the relationships between chemical compounds and biomedical terms from the literature.
These terms are MeSH (Medical Subject Headings) to index articles in the biomedical field, standardizing terms for efficient literature search and retrieval, and GO (Gene Ontology) is a standardized framework that describes gene functions across species, categorizing genes and their products based on molecular function, biological processes, and cellular components. 


## 1. CTD.py
To use this script, download the CTD file from the [CTD database](https://ctdbase.org/downloads/), remove the headers, and save it as tsv file.
This script extracts columns which contain MeSH and GO identifiers, and saves the output as _CTD_extraido.txt_.
```
python3 CTD.py CTDfile
```
Finally, remove the duplicates from the _CTD_extraido.txt_ file and save it like another file (from now on, refered as _CTD_extraido_u.txt_)

## 2. match_coincidencias.py
You need the _CTD_extraido_u.txt_ file and the _CoMent_MeshDcomp-GO_2022_s_ file which you obtain from [J.Novoa et al](https://pubmed.ncbi.nlm.nih.gov/38564426/)
_CoMent_MeshDcomp-GO_2022_s_ file contains MeSH and GO identifiers, number of articles associated with the MeSH term, with the GO term, with both terms and p-value.
The script searches for MeSH and GO terms that are common between both files and saves them in a file called _match_final.txt_
```
python3 match_coindicencias.py CoMent_MeshDcomp-GO_2022_s CTD_extraido_u.txt
```

## 3. match_vdiccplot_comorig.py
The _CTD_extraido_u.txt_ file, the _CoMent_MeshDcomp-GO_2022_s_ file, and specify the column are required if you want to represent in the graphics.
The only valid options are column five (p-value) and column four (number of articles).
```
python3 match_vdiccplot_comorig.py CoMent_MeshDcomp-GO_2022_s CTD_extraido_u.txt column_number [option_n]
```
option_n specifies what you want to represent:
- If you want to represent the number of articles, set option_n to "normal."
- If you want to represent the minimum number of articles, set option_n to "min."
- If you want to represent the p-value, leave option_n blank.

## 4. go-basic3.py
The _go-basic.obo_, which you download by [GO database](http://geneontology.org/docs/download-ontology/), is used as an argument.
This script processes the OBO file and calculates the depth of every single GO term (distance with the top term of the ontology) and saves them in a file called _output.txt_.
```
python3 go-basic3.py go-basic.obo
```

## 5. match_coment_CTDcoment_output.py
Besides _output.txt_, there is another file required as input, either _CoMent_MeshDcomp-GO_2022_s_, either _CTD_extraido_u.txt_ (first argument).
This script reads both input files, matches and combines their information and saves them as a new output file (_coment_updated.txt or CTD_updated.txt_).
```
python3 match_coment_CTDcoment_output.py first_file output.txt
```
"It is required to run this script using both CoMent and CTD input files in order to generate the two input files needed for (script number 6)

## 6. match_vdiccplot_comorig_rel.py
You need _coment_updated.txt_, _CTD_updated.txt_ and column number. The first version of this script only accepts 7 as a valid argument of column number, this being the depth of the GO terms.
This script reads two input files containing ontology data, processes and matches the data, and generates histograms to visualize the depth distributions of different ontologies across coment data, CTD data and the matches between both datasets.
```
python3 match_vdiccplot_comorig_rel.py coment_updated.txt CTD_updated.txt 7
```









