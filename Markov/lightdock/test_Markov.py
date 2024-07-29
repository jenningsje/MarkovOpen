import sys, shutil, time, subprocess, logging, os
from fetch_pdb import *
from fetch_AlphaFold import *

# change directory to app/mount/input
os.chdir("../MarkovProprietary/pipelinestages/app/mount/input")

def message(text):
    f = open("message.txt", "w")
    f.write(text)
    f.close

# fetch user input
with open("names.txt") as names:
    # read the lines of names.txt
    names_lines = names.readlines()