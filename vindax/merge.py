import os
import pandas as pd
import glob

csv_list = glob.glob('*.csv')
print(u'find %s CSV files'% len(csv_list))
for i in csv_list:
    fr = open(i,'rb').read()
    with open('result-vindax.csv','ab') as f:
        f.write(fr)
print(u'merged OK！')
