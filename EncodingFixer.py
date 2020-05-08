# -*- coding: UTF-8 -*-
import os

# Read path from file
with open('path.txt', 'r') as myfile:
    mypath = myfile.read()

files = []
for root, dirs, files in os.walk(mypath):
    for name in files:
        newpath = os.path.join(root, name)
        if (newpath.endswith('.sql')):
            from chardet.universaldetector import UniversalDetector
            detector = UniversalDetector()
            with open(newpath, 'rb') as fh:
                for line in fh:
                    detector.feed(line)
                    if detector.done:
                        break
                detector.close()
            if detector.result['encoding'] == 'UTF-8-SIG':
                s = open(newpath, mode='r', encoding='utf-8-sig').read()
                open(newpath, mode='w', encoding='utf-8').write(s)
                print('Fixed encoding in file:'+newpath)
