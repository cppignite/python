#! /usr/bin/python
'''
This project will create a ZIP file of an entire folder. This is a form
of version control where you can take snapshots of your folder so you can
keep different versions. The ZIP files will also increment each time it is 
called. (e.g backup_1.zip, backup_2.zip, etc.)

Future Extensions: Also put date on folder as well
                   Allow for user input
'''
# Step 1: Determine name for ZIP File
import zipfile, os

def backupToZip(folder):
  # Backup the entire contents of "folder" into a ZIP file.
  folder = os.path.abspath(folder)  # make sure folder is absolute

  # Figure out the filename this code should use based on what files
  # already exist
  number = 1
  while True:
    zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zipFilename):
      break
    number = number + 1
  
  # Step 2: Create the ZIP file.
  print('Creating %s...' % (zipFilename))
  backupZip = zipfile.ZipFile(zipFilename, 'w')

  # Step 3: Traverse the directory tree and add files to ZIP File
  for foldername, subfolder, filenames in os.walk(folder):
    print('Adding the files in %s...' % (foldername))
    # Add the current folder to the zip file
    backupZip.write(foldername)

    # Add all the files in this folder to the ZIP file
    for filename in filenames:
      newBase = os.path.basename(folder) + '_'
      if filename.startswith(newBase) and filename.endswith('.zip'):
        continue # don't backup the backup zip files
      backupZip.write(os.path.join(foldername,filename))
  backupZip.close()
  print('Done.')

pathName = os.path.abspath("./cuteStuff")
backupToZip(pathName)
  
