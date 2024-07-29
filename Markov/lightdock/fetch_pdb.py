import sys, shutil, time, subprocess, logging, os
sys.path.append('../MarkovProprietary/pipelinestages')
sys.path.append('..')
from gemmi import *
from fetch_from_mount import *
from fetch_from_alphafold import *

def fetch_pdb(protein, path):
    # fetch name of protein 1
    PDB_ID = search_pdb_by_protein_name(protein)

    # fetch file path of protein 1
    prot_file_path = cifDownload(PDB_ID)
    # rename protein to prot1.pdb and move file to lightdock directory
    shutil.move(prot_file_path, path)
    # move to the output directory
    os.chdir("../output")
    # tell the user that the protein is coming from the pdb
    f = open("message.txt", "w")
    f.write("fetching from the pdb...")
    f.close
    # move to the input directory
    print("fetching from the pdb...")
    os.chdir("../input")