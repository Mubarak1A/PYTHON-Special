#!/usr/bin/python3
''' Python script that check and convert all JPG
    files in a folder to PNG
'''

import sys
import os
from PIL import Image

#grap the input arguments
folder = sys.argv[1]
new_folder = sys.argv[2]

#check if new_folder already exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
    
#loop through all files in folder and convert them to png in new_folder
for file in os.listdir(folder):
    img = Image.open(f'{folder}/{file}')
    clean_name = os.path.splitext(file)
    
    img.save(f'{new_folder}/{clean_name[0]}.png')
    
    print("Done")
    