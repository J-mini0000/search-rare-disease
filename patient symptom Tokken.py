from konlpy.tag import Kkma
from itertools import chain
import re

kkma=Kkma()

inS = input('증상을 입력하세요')
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
print("b:",b)
inS_worddata=(tuple(set(b)))  # 전처리된 증상 Data 추가
print(inS_worddata)
print(type(inS_worddata))
print(inS_worddata[1])



