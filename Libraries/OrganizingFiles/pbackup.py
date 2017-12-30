#! /usr/bin/python
'''
This project will create a ZIP file of an entire folder. This is a form
of version control where you can take snapshots of your folder so you can
keep different versions. The ZIP files will also increment each time it is 
called. (e.g backup_1.zip, backup_2.zip, etc.)

Future Extensions: Also put date on folder as well
'''
# Step 1: Determine name for ZIP File
import zipfile, os

def backupToZip(folder):
# Step 2: Create the ZIP File
# Step 3: Traverse the directory tree and add files to ZIP File
