from konlpy.tag import Kkma
from itertools import chain
import re
import csv
import pandas as pd

kkma=Kkma()

inS =input("증상을 자세히 입력해주세요.\n")
    # "보톡스를 맞은 듯 달덩이 처럼 부은 얼굴, 손목은 가늘어지고 팔뚝은 오동통해지구요, 하루에 한끼만 먹는데도 임산부처럼 배가 나왔습니다. 다리도 발목은 가늘어지고 아톰다리같이 부어있어요."
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

f = open('disease.csv', 'r', encoding='utf-8-sig')
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
            if (inS_worddata[i] == disease[k][j]): #입력과 기존 데이터와 비교, 같으면~
                disease[k][j]=disease[k][j]+" True"
                disease[len(disease) - 1][j] = int(disease[len(disease) - 1][j]) + 1 #마지막행에 +1

fresult = disease[len(disease)-1]
print("fresult",fresult)
result = pd.DataFrame(disease)
result.to_csv('./result.csv', index=False, sep=',', na_rep='NaN',header=None, encoding='utf-8-sig')
print('result:',result)

print(

)
