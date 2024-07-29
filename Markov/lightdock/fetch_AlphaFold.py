import sys, shutil, time, subprocess, logging, os
sys.path.append('../MarkovProprietary/pipelinestages')
sys.path.append('..')
from gemmi import *
from fetch_from_mount import *
from fetch_from_alphafold import *
import shutil
import os

def fetch_AlphaFold(protein, path):
    # retrieve the file path for the pdb file
    prot_file_path = get_AlphaFold_data(protein)
    # rename protrein to prot1
    shutil.move(prot_file_path, path)
    os.chdir("../output")
    f = open("message.txt", "w")
    f.write("file not available on the protein databank fetching file from the alphafold databank instead")
    f.close
    print("file not available on the protein databank fetching file from the alphafold databank instead")
    os.chdir("../input")