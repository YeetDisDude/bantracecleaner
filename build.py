import os
import shutil

SPECFILE = "main.spec"
DISTFOLDER = "dist"
BUILDFOLDER = "build"

print("Building...")
os.system('pyinstaller --onefile --icon="icon.ico" main.py')

target_folder = os.path.abspath(os.path.join(DISTFOLDER, os.pardir))
source_file = os.path.join(DISTFOLDER, "main.exe")
destination_file = os.path.join(target_folder, "bantracecleaner.exe")

shutil.move(source_file, destination_file)
print("Moved exe to this folder")
print("Cleaning up...")

if os.path.exists(SPECFILE):
    os.remove(SPECFILE)
    print(f"File '{SPECFILE}' deleted successfully.")
else:
    print(f"File '{SPECFILE}' not found.")

if os.path.exists(DISTFOLDER):
    shutil.rmtree(DISTFOLDER)
    print(f"Folder '{DISTFOLDER}' deleted successfully.")
else:
    print(f"Folder '{DISTFOLDER}' not found.")

if os.path.exists(BUILDFOLDER):
    shutil.rmtree(BUILDFOLDER)
    print(f"Folder '{BUILDFOLDER}' deleted successfully.")
else:
    print(f"Folder '{BUILDFOLDER}' not found.")
