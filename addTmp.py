#!/home/dopel/venv/scripts/bin/python3.8

from os import listdir, getcwd, remove, stat
from os.path import exists
from datetime import datetime
# agregar fechas despues

current_path = getcwd()

if __name__== '__main__':
    if exists(current_path + '/currentFile.txt'):
        objFile = open(current_path + '/currentFile.txt', mode='+a')
        objFile.writelines('\n')
    else:
        objFile = open(current_path + '/currentFile.txt', mode='+w')
    list_files = listdir(current_path)
    for item in list_files:
        lines = []
        if item == 'currentFile.txt':
            continue
        else:
            tmpFile = open(current_path + '/' + item)
            lines.append(tmpFile.readline()) 
            tmpFile.close()
    for line in lines:
        objFile.writelines(line)
        objFile.writelines('\n')
    objFile.close()
    if stat(current_path + '/currentFile.txt').st_size != 0:
        for item in list_files:
            if item == 'currentFile.txt':
                continue
            else:
                remove(current_path + '/' + item)
