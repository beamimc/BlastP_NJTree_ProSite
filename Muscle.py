##Function to align and make NJ trees 
import os
from subprocess import Popen, PIPE, call

def Muscle():
    #second align each multifasta file 
    os.makedirs("Results/Aligments", exist_ok=True)
    files = os.listdir("Results/Blast_Hits/")
    for file in files:
        name_result = "Results/Aligments/" + file +"_aligned"
        hits_to_align = "Results/Blast_Hits/" + file
        call(['muscle','-in', hits_to_align,'-out', name_result, '-verbose'], stderr=open("log", 'a+'), stdout=open("log", 'a+'))
       
        print("alignment of "+file+" done\n")  
    
    ##make NJ tree
    os.makedirs("Results/NJTrees", exist_ok=True)
    aligments = os.listdir("Results/Aligments/")
    for aligment in aligments:
        name_result = "Results/NJTrees/"+ aligment + "_NJtree"
        call(['muscle', '-maketree', '-in', 'Results/Aligments/'+aligment, '-out', name_result, '-cluster', 'neighborjoining'], stderr=open("log", 'a+'), stdout=open("log", 'a+'))
        print("NJ tree of "+ aligment+ " done\n")
    
    return
