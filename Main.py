###MAIN PROGRAM
import sys 
import os
import argparse
import datetime

import project.GenBank as gnk
import project.BlasterP as blst
import project.Muscle as mscl
import project.Prosite as prst

def Main(folder, qcovs, pident):
    blst.BlasterP(folder, qcovs, pident)
    mscl.Muscle()
    prst.Prosite_parser()
    print("-------------Done!-------------")
    return

def split_querys(input_fasta):
    with open(input_fasta,"r") as multifasta:
        querys=multifasta.read().splitlines()
        for i in range(0,len(querys)-2,2):
            name="Data/Query_"+str(int(i/2 + 1))
            query_i=open(name,"w")
            query_i.write("%s\n%s\n" % (querys[i], querys[i+1]))
            query_i.close()
    return

def check_fasta(file):
    with open(file,"r") as file_handler:
        lines=file_handler.read().splitlines()
        if lines[0][0]==">":
            return(True)
        else:
            return(False)

################################
#####input control and help#####
################################
parser = argparse.ArgumentParser(description='Paquete de pyhton que, dadas unas secuencias \
    query en un archivo multifasta y una carpeta con archivos genbank: parsea y obtiene los CDS\
    de cada archivo genbank, y realiza un BlasP para cada secuencia query contra esos CDS. Los resultados del blast\
    se filtran por porcentaje de indentidad y de covertura. Con los hits obtenidos en el blast se hace\
    un alineamiento de secuencias y un NJ tree para cada blast (uno por query). Finalmente, para cada proteina\
    hit en los blastp, se hace una búsqueda de sus dominios utilizando la base de datos de dominios de ProSite.')

parser.add_argument("-query", type=str, help="Archivo fasta o multifasta que contiene las querys.")
parser.add_argument("-genbank", type=str, help="Carpeta que unicamente contiene archivos tipo genbank de los que extraer los CDS.")
parser.add_argument("-pident", type=float, help="Porcentage de indentidad con el que filtrar el BlastP.\n\
    Si no se especifica, el valor por defecto es 30.")
parser.add_argument("-qcovs", type=float, help="Porcentage de indentidad con el que filtrar el BlastP.\n\
    Si no se especifica, el valor por defecto es 0.")


##################
## main program ##
##################
args = parser.parse_args()
if (args.query==None) & (args.genbank==None):
    print("Debe introducir un archivo con secuencias query: -query QUERY.\n\
        Debe introducir una carpeta con archivos tipo genbank: -genbank GENBANK\n\
        Pruebe -h para obtener ayuda.\n")
    exit()
elif (args.query==None) & (args.genbank!=None):
    print("Debe introducir un archivo con secuencias query: -query QUERY.\n\
           Pruebe -h para obtener ayuda.\n")
    exit()
elif (args.query!=None) & (args.genbank==None):
    print("Debe introducir una carpeta con archivos tipo genbank: -genbank GENBANK\n\
        Pruebe -h para obtener ayuda.\n")
    exit()

if not check_fasta(args.query): ##check if input is a fasta file
    print("Debe introducir como -query un archivo tipo fasta o multifasta\n\
        Pruebe -h para obtener ayuda.\n")
    exit()
if not os.path.exists(args.genbank): ##check if input is a real directory
    print("Debe introducir como -genbank el path de una carpeta que contenga archivos tipo genbank\n\
        Pruebe -h para obtener ayuda.\n")
    exit()

#create directories 
os.makedirs("Results", exist_ok=True)
os.makedirs("Data", exist_ok=True)
#create log file for the execution
log = open("log","w")
log.write("Log file. Execution date: %s\n" % (datetime.datetime.now()))

split_querys(args.query)
Main(args.genbank, args.qcovs, args.pident)

log.close()