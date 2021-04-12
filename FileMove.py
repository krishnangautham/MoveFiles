import glob, shutil, os, sys

if len(sys.argv) == 3:
    file_regex = sys.argv[1]
    destination_folder = sys.argv[2]
    print(file_regex)
    print(destination_folder)
    # Returns a list of names in list files.
    files = glob.glob(file_regex, recursive = True)
    for file in files:
        shutil.move(file, destination_folder)
else:
    print('You need to include a path to the files to move and a destination folder path.')
    exit(2)
