#테스트용 파일
from konlpy.tag import Kkma
from itertools import chain
import re
import csv

kkma=Kkma()

inS = '두통 및 치통이 있어요'
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
    disease.append(exel)
f.close()

for i in range(len(inS_worddata)):
    print(len(inS_worddata))
    for j in range(1,len(disease[0])): #11
        for k in range(len(disease)): #385
            if (inS_worddata[i] == disease[k][j]):
                disease[k+1][j] = disease[k+1][j]+1



