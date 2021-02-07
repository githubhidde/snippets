from zipfile import ZipFile
import os

# create a ZipFile object
zipObj = ZipFile(r'd:\_test_dir\sample.zip', 'w')
print("d:\_test_dir\sample.zip' is temporarily created")
# Add multiple files to the zip
zipObj.write(r'C:\_test_dir\test123.txt')
zipObj.write(r'C:\_test_dir\test_1.log')
print("log files are added to the zip file")

#close the Zip File
zipObj.close()

# Extract the zip file to a given location
zf = ZipFile(r'd:\_test_dir\sample.zip', 'r')
zf.extractall(r'c:\EDV')
print("Content is written in " + r'c:\EDV\test_dir')
zf.close()
print('Done!') 

# Delete temporary file location
myfile=r'd:\_test_dir\sample.zip'

## If file exists, delete it ##
if os.path.isfile(myfile):
	os.remove(myfile)
	print("r'd:\_test_dir\sample.zip' + is cleaned up!")
else:    ## Show an error ##
	print("Error: %s file not found" % myfile)