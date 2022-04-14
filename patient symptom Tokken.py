from konlpy.tag import Kkma
from itertools import chain
import re
import csv
import pandas as pd

kkma=Kkma()

inS = "두통 복통"
inS_wordlst=inS.split()
print(inS_wordlst)
inS_worddata=[]
sentence = []
nouns = []
for i in inS_wordlst:
    sentence.append(re.sub('[^A-Za-z가-힣]', '', i))
print(sentence)
for i in sentence:
    nouns.append(kkma.nouns(i))  # 명사분리후 리스트에 추가
print(nouns)
b = list(chain(*nouns))  # 1차원 list
# print("b:",b)
inS_worddata=(list(set(b)))  # 전처리된 증상 Data 추가
print(inS_worddata)

f = open('disease.csv', 'r', encoding='utf-8')
crd = csv.reader(f)
disease = []
for exel in crd:
    print(exel)
    disease.append(exel)
f.close()
print(len(disease))
for i in range(0,len(inS_worddata)):
    print("ins~[i]",inS_worddata[i])
    for j in range(0,len(disease[0])-1): #1~386
        for k in range(1,len(disease)-1): #1~10
            print('%d'%(k),inS_worddata[i] == disease[k][j])
            if (inS_worddata[i] == disease[k][j]):
                disease[len(disease)-1][j]=int(disease[len(disease)-1][j])+1
result = pd.DataFrame(disease)
result.to_csv('./result.csv', index=False, sep=',', na_rep='NaN')
print(disease)






