from fetch_from_mount import *
import shutil
import os

# change directory to app/mount/input
os.chdir("app/mount/input")

def message(text):
    f = open("message.txt", "w")
    f.write(text)
    f.close

# fetch user input
with open("names.txt") as names:
    # read the lines of names.txt
    names_lines = names.readlines()

# fetch name of protein 1
PDB_ID = search_pdb_by_protein_name("Crystal structure of S. pyogenes Cas9")

# fetch file path of protein 1
prot_file_path = cifDownload(PDB_ID)
# rename protein to prot1.pdb and move file to lightdock directory
shutil.move(prot_file_path, "../../../../../lightdock/prot1.pdb")
print(os.getcwd())
os.chdir("../output")
message("fetching from the pdb...")
print("fetching from the pdb...")
os.chdir("../input")