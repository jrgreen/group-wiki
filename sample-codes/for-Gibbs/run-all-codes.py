import os
import shutil

for i in range(10):
    fname = "data-file-%d.csv" % (i + 1)
    os.system('python sample-python-code.py')
    shutil.move('data-file.csv', fname)




