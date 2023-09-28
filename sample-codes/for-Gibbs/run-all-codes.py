import os
import shutil

for i in range(10):
    fname = "dissipation-data-eta-0-5-eta-1-2-10-5-optimized-%d.csv" % (i + 1)
    os.system('python thermostat-0532-dissipation-eta-optimized.py')
    shutil.move('dissipation-data-eta-0-5-eta-1-2-10-5-optimized-0.csv', fname)




