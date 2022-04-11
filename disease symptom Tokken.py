from konlpy.tag import Kkma
from itertools import chain
import re
import pandas as pd
kkma=Kkma()
pd.set_option('display.max_rows', None)
def dataPrep(openfile):
    sentence = []
    nouns = []
    for i in openfile:
        sentence.append(re.sub('[^A-Za-z가-힣]', '', i))
    for i in sentence:
        nouns.append(kkma.nouns(i))  # 명사분리후 리스트에 추가
    b = list(chain(*nouns))  # 1차원 list
    data_wordlst.append(list(set(b))) #전처리된 증상 Data 추가
    # data_wordlst=[data_word,data_word1,data_word2,data_word3...]
    return b

cf0 = open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/Cushing's syndrome symptomIFile.txt", 'r', encoding='utf-8') #txt파일 열어 읽기
cf1 = open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/Crohn's disease.txt", 'r', encoding='utf-8')
cf2= open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/multiple sclerosis.txt", 'r', encoding='utf-8')
cf3= open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/MoyaMoya.txt", 'r', encoding='utf-8')
cf4= open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/Idiopathic pulmonary fibrosis.txt", 'r', encoding='utf-8')
cf5= open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/Guillian Barre syndrome.txt", 'r', encoding='utf-8')
cf6= open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/Haemophilia.txt", 'r', encoding='utf-8')
cf7= open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/dilated cardiomyopathy.txt", 'r', encoding='utf-8')
cf8= open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/Systemic lupus erythematosus.txt", 'r', encoding='utf-8')
cf9= open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/myasthenia gravis.txt", 'r', encoding='utf-8')

data_wordlst=[] #전처리된 증상Data 들어갈 빈배열 선언

dataPrep(cf0),dataPrep(cf1),dataPrep(cf2),dataPrep(cf3),dataPrep(cf4),dataPrep(cf5),dataPrep(cf6),dataPrep(cf7),dataPrep(cf8),dataPrep(cf9),


disease = pd.DataFrame(columns = ['쿠싱증후군', #열
                                  '크론병',
                                  '다발성 경화증',
                                  '모야모야병',
                                  '특발성 폐섬유화증',
                                  '길렝-바레 증후군',
                                  '혈우병(제 8,9인자 결함)',
                                  '확장성 심근병증',
                                  '전신홍반루푸스',
                                  '중증근무력증'])

bigger=0
biggerlst=data_wordlst[0]

for i in range(0,len(data_wordlst)):
    if (len(biggerlst) < len(data_wordlst[i])) == True:
        bigger = len(data_wordlst[i])
        biggerlst = data_wordlst[i]
    else:
        bigger = len(biggerlst)
        biggerlst = biggerlst

for i in range(0,len(data_wordlst)):
    if data_wordlst[i]!=biggerlst:
        for j in range(len(data_wordlst[i]),bigger):
            data_wordlst[i].append(None)

for k in range(bigger):
    insert = {'쿠싱증후군': data_wordlst[0][k],
              '크론병':data_wordlst[1][k],
              '다발성 경화증':data_wordlst[2][k],
              '모야모야병':data_wordlst[3][k],
              '특발성 폐섬유화증':data_wordlst[4][k],
              '길렝-바레 증후군':data_wordlst[5][k],
              '혈우병(제 8,9인자 결함)':data_wordlst[6][k],
              '확장성 심근병증':data_wordlst[7][k],
              '전신홍반루푸스':data_wordlst[8][k],
              '중증근무력증':data_wordlst[9][k]}

    disease = disease.append(insert, ignore_index=True)
disease.to_csv('C:/Users/hw499/PycharmProjects/CapstoneDesign/disease.csv',sep=',',na_rep='NaN')
print(disease)