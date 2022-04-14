from konlpy.tag import Kkma
from itertools import chain
import re
import csv
import pandas as pd

f = open('result.csv', 'r', encoding='utf-8')
crd = csv.reader(f)
result = []
for exel in crd:
    print(exel)
    result.append(exel)
f.close()

print(result)