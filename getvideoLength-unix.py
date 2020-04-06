import os
import sys

currentDir = os.getcwd()
getallfiles = [x for a, b, c in os.walk(currentDir) for x in c]

with open('files.txt', 'w') as vi:
    for file in getallfiles:
        NewFile = file.replace(' ', '\ ')
        n2 = NewFile.replace('(', '\(')
        n3 = n2.replace(')', '\)')
        command = f'exiftool {n3} | grep Duration'
        # print(command)
        f = os.popen(command)
        length = f.read()[:41][-7:]
        # print(f'{file} \n{length}')

        vi.write(f'{file} \n{length}\n')
