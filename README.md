# BlastP_NJTree_ProSite
Paquete de pyhton que, dadas unas secuencias query en un archivo multifasta y una carpeta con archivos genbank: parsea y obtiene los CDS de cada archivo genbank, y realiza un BlasP para cada secuencia query contra esos CDS. Los resultados del blast se filtran por porcentaje de indentidad y de covertura. Con los hits obtenidos en el blast se hace un alineamiento de secuencias y un NJ tree para cada blast (uno por query). Finalmente, para cada proteina hit en los blastp, se hace una búsqueda de sus dominios utilizando la base de datos de dominios de ProSite.

Para la correcta ejecución:
- 
        - En el path de ejecución debe colocarse la carpeta Prosite_DB (que se adjunta) descomprimida.
        - En el path donde se ubique el Main debe colocarse la carpeta project, 
        para poder acceder a los distintos módulos. 

        - Las secuencias query deben darse en un único archivo mutlifasta.
        - Los archivos .gbff que se deseen utilizar para obtener los CDS deben colocarse todos en 
        una misma carpeta. La carpeta no debe contener nada más.
        - Es posible introducir los valores deseados de filtrado en el porcentaje de identidad y 
        de coverage para el BlastP. Si no se indican, los valores por defecto son 30 y 0 respectivamente.

En el path de ejecución se creará:
-
        - un archivo log.
        - una carpeta Data: que contendrá la o las querys utilizadas.
        - una carpeta Results: que contendrá a su vez:
                        - un archivo multifasta con los CDS.
                        
                        - carpeta BlastP_results: donde se guardan los resultados filtrados del blastP 
                        para cada query.
                        
                        - carpeta Blast_Hits: donde se guardan los archivos que contienen las secuencias 
                        proteicas de los hits + query de cada blast.
                        
                        - carpeta Aligments: donde se guardan los archivos con hits alineados con MUSCLE.
                        
                        - carpeta NJTrees: con los resultados del MUSCLE NJTree.
                        
                        - carpeta Protein_Domains: donde se guardan los archivos que contienen los 
                        dominios de cada proteina obtenidos parseando ProSite.

