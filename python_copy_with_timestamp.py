# importing os module and makedirs function
from os import makedirs
import os
# method which creates a directory with a timestamp
from datetime import datetime

today = datetime.now
new_run = r"D:\_test_dir\{}" .format(today().strftime('%Y_%m_%d_%H_%M'))
makedirs(new_run, exist_ok=True)

# importing shutil module
import shutil

# Source path 
source = r'C:\_test_dir\test123.txt'

# Print the metadeta 
# of source file 
metadata = os.stat(source)
print("Metadata:", metadata, "\n") 

# Destination path
destination = new_run

# Copy the content of 
# source to destination
dest = shutil.copy2(source, destination)

# Print the metadata 
# of the destination file
matadata = os.stat(destination) 
print("Metadata:", metadata, "\n")

# Print path of source  
# copied file
print("Source path:", source, "\n") 

# Print path of newly  
# created file 
print("Destination path:", dest) 