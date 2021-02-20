#!/home/dopel/venv/scripts/bin/python3.8

from sys import argv
from os import getcwd, mkdir, chdir
from time import ctime

current_path = getcwd()
dirs = ['assetsNscript', 'code', 'scrappyData', 'cleanData']
files = ['log.md', 'readme.md']
project_name = argv[1]

if __name__ == '__main__':
    mkdir(current_path + '/' + project_name)
    chdir(current_path + '/' + project_name)
    current_path = getcwd()
    for item in dirs:
        mkdir(current_path + '/' + item)
    for item in files:
        objFile = open(current_path + '/' + item, mode='w')
        objFile.writelines('Name Project : ' + project_name + '\n')
        objFile.writelines('Date : ' + ctime())
        objFile.close()
