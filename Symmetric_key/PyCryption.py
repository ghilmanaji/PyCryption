import os
from pathlib import Path
from cryptography.fernet import Fernet
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)

basepath1 ="Input_Encrypt"
basepath2 ="Output_Encrypt"
list_folder=[]
for entry in os.listdir(basepath1):
    if os.path.isfile(os.path.join(basepath1,entry)):
                with open(basepath1+"/"+entry, 'rb') as file:
                    original = file.read()
                encrypted = fernet.encrypt(original)
                with open(basepath2+"/"+entry+'.aji', 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
for entry in os.listdir(basepath1):
        if os.path.isdir(os.path.join(basepath1, entry)):
            enum_folder=0
            list_folder.insert(enum_folder,entry)
for folder in list_folder:
    path1="Input_Encrypt/"+folder
    path2="Output_Encrypt/"+folder
    os.mkdir(path2)
    for entry in os.listdir(path1):
        if os.path.isfile(os.path.join(path1, entry)):
            with open(path1+"/"+entry, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(path2+"/"+entry+'.aji', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)