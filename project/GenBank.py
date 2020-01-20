##GenBank parser fuction
import sys
from Bio import Seq
from Bio import SeqIO
import os


def Parser(folder):
    #fucntion to extrar CDS from one or multiple genbank files, given a directory
    output = "Results/CDS.fa"
    output_handle = open(output, "w")
    Path = os.getcwd()
    folder_path = Path + "/" + folder
    filelist = os.listdir(folder_path)
    
    for x in filelist:
        print("parsing " + x)
        parsing = folder_path + x
        with open(parsing,"r") as input_handle:
            for seq_record in SeqIO.parse(input_handle,"genbank"):
                for seq_feature in seq_record.features:
                    if seq_feature.type=="CDS":
                        try: ##to avoid pseudogens whithout \translation
                            #create multifasta file
                            output_handle.write(">%s-%s\n%s\n" % ( 
                            seq_record.name,
                            seq_feature.qualifiers['locus_tag'][0],
                            seq_feature.qualifiers['translation'][0]))
                        except:
                            pass
        output_handle.close()
        print("Done parsing\n")
    return output