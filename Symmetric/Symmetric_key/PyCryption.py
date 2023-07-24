# import library
import os
from pathlib import Path
from cryptography.fernet import Fernet

# import key to do encryption
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)

# path input and output
basepath1 ="Input_Encrypt"
basepath2 ="Output_Encrypt"
os.mkdir(basepath2)

# define list folder
list_folder=[]

# encrypt
for entry in os.listdir(basepath1):
    if os.path.isfile(os.path.join(basepath1,entry)):
                with open(basepath1+"/"+entry, 'rb') as file:
                    original = file.read()
                encrypted = fernet.encrypt(original)
                with open(basepath2+"/"+entry+'.aji', 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
    if os.path.isdir(os.path.join(basepath1, entry)):
        path1_1=basepath1+"/"+entry
        path2_1=basepath2+"/"+entry
        os.mkdir(path2_1)
        for entry in os.listdir(path1_1):
                if os.path.isfile(os.path.join(path1_1, entry)):
                    with open(path1_1+"/"+entry, 'rb') as file:
                        original = file.read()
                    encrypted = fernet.encrypt(original)
                    with open(path2_1+"/"+entry+'.aji', 'wb') as encrypted_file:
                        encrypted_file.write(encrypted)
                if os.path.isdir(os.path.join(path1_1,entry)):
                    path1_2=path1_1+"/"+entry
                    path2_2=path2_1+"/"+entry
                    os.mkdir(path2_2)
                    for entry in os.listdir(path1_2):
                        if os.path.isfile(os.path.join(path1_2, entry)):
                            with open(path1_2+"/"+entry, 'rb') as file:
                                original = file.read()
                            encrypted = fernet.encrypt(original)
                            with open(path2_2+"/"+entry+'.aji', 'wb') as encrypted_file:
                                encrypted_file.write(encrypted)
