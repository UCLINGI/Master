import sys, os.path, os,shutil
import re

def toDirName(name):
    name = name.replace(" ","_")
    name = re.sub("[é|è]","e",name)
    name = re.sub(r"[^a-zA-Z0-9\(\)\[\]\_]","e",name)
    
    return name

def acceptableName(name):
    if len(name)>0:
        return True
    else: 
        return False


if len(sys.argv) < 2:
    print("Usage : python3 addDocs.py path/to/dest/dir \n");

destDir = sys.argv[1]
if(not os.path.isdir(destDir)):
    print("Error : " + destDir + " is not a directory\n")

ressourcesDir = os.path.join(os.path.dirname(os.path.dirname(sys.argv[0])), "EmptyDoc")


print("Please enter your document name:");
docName = input();
acceptedName = False;
while(acceptedName == False):
    if(not acceptableName(docName) ):
        print("This name is not correct\n")
    else:
        print("Whould you like to create a directory " + toDirName(docName) + " with the document in " + destDir  + " ? [y/n]")
        resp = input()
        if resp[0] == 'y':
            acceptedName = True;
            break
    print("Please enter your document name")
    docName = input();

docDir = os.path.join(destDir,toDirName(docName))

os.mkdir(docDir)
links = ["eplDoc.cls" , "logo_ucl.jpg"]
for link in links:
    ressourceFile = os.path.join(ressourcesDir,link)
    docFile       = os.path.join(docDir,link)
    os.symlink(os.path.relpath(ressourceFile,docDir), docFile)

shutil.copy(os.path.join(ressourcesDir,"document.tex"), docDir)

print("done")
