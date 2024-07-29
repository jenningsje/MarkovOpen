import sys, shutil, time, subprocess, logging, os
sys.path.append('../MarkovProprietary/pipelinestages')
sys.path.append('..')
from gemmi import *
from fetch_from_mount import *
from fetch_from_alphafold import *

def create_empty_file(file_name):
    try:
        with open(file_name, 'w') as f:
            pass  # This creates an empty file
        print(f"Empty file '{file_name}' created successfully.")
    except IOError:
        print(f"Unable to create empty file '{file_name}'.")

# Example usage:
file_name = "empty_file.txt"
create_empty_file(file_name)

def message(text):
    f = open("message.txt", "w")
    f.write(text)
    f.close

def fetch_pdb(name, pdb_file):
    lightdock_path = os.path.abspath("../../../../../lightdock")
    # attempt to fetch the name of the protein from the protein databank
    try:
        # fetch name of protein 1
        PDB_ID = search_pdb_by_protein_name(name)
        # fetch file path of protein 1
        prot_file_path = cifDownload(PDB_ID)
        # rename protein to prot1
        os.rename(prot_file_path, pdb_file)
        # move file to lightdock
        shutil.move(pdb_file, lightdock_path)
        # tell user that the file is available on the protein databank
        os.chdir("../output")
        message("fetching from the pdb...")
        print("fetching from the pdb...")
        os.chdir("../input")
    except:
        # attempt to fetch the name of the protein from the AlphaFold databank
        try:
            # retrieve the file path for the pdb file
            prot_file_path = get_AlphaFold_data(name)
            # rename protrein to prot1
            os.rename(prot_file_path, pdb_file)
            # move file to lightdock
            shutil.move(pdb_file, lightdock_path)
            # tell user that the file is available in the alphafold databank
            os.chdir("../output")
            message("file not available on the protein databank fetching file from the alphafold databank instead")
            print("file not available on the protein databank fetching file from the alphafold databank instead")
            os.chdir("../input")
        # send error message to the front end if the pdb does not exist
        except:
            os.chdir("../output")
            message("that protein does not exist in the protein databank or the alphafold databank, please try another query")
            print("that protein does not exist in the protein databank or the alphafold databank, please try another query")
            os.chdir("../input")

os.chdir('../MarkovProprietary/pipelinestages/app/mount/input')
print("success")

from_alphafold = "file not available on the protein databank fetching file from the alphafold databank instead"

from_pdb = "fetching from the pdb..."

def Markov():
    while True:
        # erase the data from names.txt
        with open("names.txt", "w"):
            pass 

        # fetch user input
        names = open("names.txt")
        names_lines = names.readlines()
        
        # erase the data from the message
        with open("../output/message.txt", "w") as message:
            message.write("fetch the next two proteins...")
            print("fetch the next two proteins...")

        # read the message
        message = open("../output/message.txt")
        message_line = message.readlines()
    
        # Fetch the first protein
        while (message_line[0] != (from_alphafold or from_pdb)):
            # open the message file
            message = open("../output/message.txt")
            message_line = message.readlines()
            # read the names of the input
            names_lines = names.readlines()
            print("message")
            print(message_line[0])
            time.sleep(1)
            try:
                fetch_pdb(names_lines[0], "prot1.pdb")
            except:
                print("no input")

        # erase the data from names.txt
        print("test")
        with open("names.txt", "w"):
            pass 
        
        # take in input from names.txt
        next_names = open("names.txt")
        next_lines = next_names.readlines()
        print(next_lines)

        # fetch the current signal from the front end
        from_front_end = open("../output/from_front_end.txt")
        from_front_end_lines = from_front_end.readlines()

        # wait for signal from front end to arrive to the backend
        while (from_front_end_lines[0] != (from_alphafold or from_pdb)):
            print(from_front_end_lines[0])
            print("inside the for loop")
            from_front_end = open("../output/from_front_end.txt")
            from_front_end_lines = from_front_end.readlines()
            time.sleep(5)

        # read the message
        with open("../output/message.txt", "w") as message:
            message.write("fetch the next protein")

        # Fetch the second protein
        while len(next_lines) == 0:
            # If there are no lines left, wait for a certain amount of time before checking again
            time.sleep(1)
            next_names = open("names.txt")
            next_lines = next_names.readlines()
            print("length of next lines")
            print(len(next_lines))

        fetch_pdb(next_lines[0], "prot2.pdb")

        os.chdir("../../../../../lightdock")
        while not os.path.isfile("ping.json"):
            print("waiting for signal")
        
        print("fetching pdbs...")
        subprocess.run(["python", "Run_Markov.py"])
        print("setting up lightdock...")
        subprocess.run(["lgd_setup.py", "-s", "1", "-g", "200", "prot1.pdb", "prot2.pdb", "--now", "--noh"])
        print("running lightdock...")
        subprocess.run(["lgd_run.py", "-s", "scoring.conf", "setup.json", "10", "-c", "2"])
        print("generate conformations")
        os.chdir("swarm_0")
        subprocess.run(["lgd_generate_conformations.py", "../prot1.pdb", "../prot2.pdb", "gso_10.out", "1"])

if __name__ == "__main__":
    Markov()