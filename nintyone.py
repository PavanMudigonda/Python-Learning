import os.path
if os.path.isfile('test.txt'):
    print('The file exists')


import os.path
if os.path.isfile('test.txt'):
    os.remove('test.txt')


printfile myfile.txt


import sys
with open(sys.argv[1],'r') as input_file:
    print(input_file.read())


import sys with open(sys.argv[1],'r') as input_file: print(input_file.read())
