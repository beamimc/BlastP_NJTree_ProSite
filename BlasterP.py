##BlasterP function
import sys 
import os

from Bio import Seq
from Bio import SeqIO
from subprocess import Popen, PIPE, call
import pandas as pd

import project.GenBank as gnk

def BlasterP(folder, qcovs, pident):
    #function to blastp
    os.makedirs("Results/BlastP_Results", exist_ok=True)
    subject = gnk.Parser(folder)
    query_list = os.listdir("Data/")

    for query in query_list:
        name_result="Results/BlastP_Results/BlastP_" + query
        query="Data/" + query
        proceso = Popen(['blastp','-query',query,'-subject',subject,'-outfmt',"6 qseqid qcovs pident evalue sseqid sseq" ], stdout=PIPE, stderr=open("log", 'a+'))
       
        listado = proceso.stdout.read()
        proceso.stdout.close()
       
        output = open(name_result, "w")
        output.write("qseqid\tqcovs\tpident\tevalue\tsseqid\tsseq\n")
        output.write(listado.decode('utf-8'))
        output.close()

        #filter blastp
        ##if no values given, stablish default filter
        if qcovs==None:
            qcovs=0
        if pident==None:
            pident=30

        df1 = pd.read_csv((name_result), delimiter='\t')
        filtered = df1.loc[(df1.pident >= pident) & (df1.qcovs >= qcovs) & (df1.evalue <= 0.000001)]
        filtered.to_csv(name_result+'.tsv',sep='\t', index=False)
        os.remove(name_result)
        print ("BlastP of "+query +" done")  

        #create multifasta with the hits and the query
        extract_hits(query, name_result+'.tsv')
        
    return

def extract_hits(query, blastp_result):
    #Function to create multifasta files with protein hits from each BlastP + their query
    query_handle = open(query, "r")
    name_query=query[5:]
    os.makedirs("Results/Blast_Hits", exist_ok=True)

    cds_seqs = open("Results/CDS.fa", "r")
    cds_seqss = cds_seqs.read().splitlines()

    name_hits_result="Hits_of_"+ name_query
    hits_file = open("Results/Blast_Hits/"+ name_hits_result, "w")
    hits_file.write(query_handle.read())
    blastp_result = open(blastp_result, "r")
    for row in blastp_result:
        row=row.split("\t")
        Hit=">"+str(row[4])
        for i in range(len(cds_seqss)):
            if cds_seqss[i]==Hit:
                hits_file.write("%s\n%s\n" % (cds_seqss[i], cds_seqss[i+1]))
                break
            else:
                pass
    hits_file.close()
    blastp_result.close()
    print(name_hits_result+ " extracted\n")
    cds_seqs.close()

    return