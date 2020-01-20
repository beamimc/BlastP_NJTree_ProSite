##Function to find protein domains
import os
import re

from Bio.ExPASy import Prosite, Prodoc


def Prosite_parser():
	#function to parse protein domains usind ProSite database
	prosite_handle = open("Prosite_DB/prosite.dat","r")
	records = Prosite.parse(prosite_handle)

	os.makedirs("Results/Protein_Domains", exist_ok=True)
	file_list = os.listdir("Results/Blast_Hits/")
	substitutions = {"-":"", "{":"[^", "}":"]", "(":"{", ")":"}","X":".","x":".","<":"^",">":"$"}
				
	for file in file_list:
		file_handle = open('Results/Blast_Hits/'+file,'r')
		cds_seqs = file_handle.read().splitlines()

		for i in range(0,len(cds_seqs),2):
			print("Parsing domains of "+cds_seqs[i][1:])
			result_name="Results/Protein_Domains/"+cds_seqs[i][1:]+"_domains"
			protein = open(result_name,"w")
			sequence = cds_seqs[i+1]
			for record in records:
				pattern = record.pattern[:-1]
				for key in substitutions.keys():
					pattern = pattern.replace(key, substitutions[key]) 
				if re.search(pattern, sequence):
					protein.write("Name: %s\nAccesion: %s\nDescription: %s\nPattern: %s\n\n" % ( 
                            record.name,
                            record.accession,
                            record.description, 
							pattern))	
				else:
					pass
			print("Domains parsed\n")
			protein.close()
	prosite_handle.close()

	return

