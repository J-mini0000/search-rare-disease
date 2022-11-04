from konlpy.tag import Kkma
from itertools import chain
import re
import pandas as pd

kkma=Kkma()
pd.set_option('display.max_rows', None)
stopwords = ['랫','게','건','루','기와','만','타','나중','이외','년','랭','만일','만','르','마지막','것','의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','로','자','에','와','한','하다','을','그','다','니','및','하면서',"경우","다",'니','그','과','에도','오히려','또한','또','거나','때문','듯이','니다','되','데','위의']
def dataPrep(openfile):
    sentence = []
    nouns = []
    for i in openfile:
        sentence.append(re.sub('[^A-Za-z가-힣]', ' ', i))
    for j in sentence:
        # 명사분리 및 불용어 처리
        token=kkma.nouns(j)
        token=[t for t in token if t not in stopwords]
        nouns.append(token)
    b = list(chain(*nouns))  # 1차원 list
    data_wordlst.append(list(set(b))) #전처리된 증상 Data 추가
    # data_wordlst=[data_word,data_word1,data_word2,data_word3...]
    return b

cf0 = open("./SymptomFile/Cushing's syndrome symptomIFile.txt", 'r', encoding='utf-8') #txt파일 열어 읽기
cf1 = open("./SymptomFile/Crohn's disease.txt", 'r', encoding='utf-8')
cf2 = open("./SymptomFile/multiple sclerosis.txt", 'r', encoding='utf-8')
cf3 = open("./SymptomFile/MoyaMoya.txt", 'r', encoding='utf-8')
cf4 = open("./SymptomFile/Idiopathic pulmonary fibrosis.txt", 'r', encoding='utf-8')
cf5 = open("./SymptomFile/Guillian Barre syndrome.txt", 'r', encoding='utf-8')
cf6 = open("./SymptomFile/Haemophilia.txt", 'r', encoding='utf-8')
cf7 = open("./SymptomFile/dilated cardiomyopathy.txt", 'r', encoding='utf-8')
cf8 = open("./SymptomFile/Systemic lupus erythematosus.txt", 'r', encoding='utf-8')
cf9 = open("./SymptomFile/myasthenia gravis.txt", 'r', encoding='utf-8')

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

bigger=0                                                #bigger 0으로 초기화
biggerlst=data_wordlst[0]                               #biggerlst를 data_wordlst의 index 0으로 초기화
for i in range(0,len(data_wordlst)):                    #data_wordlst의 원소중 가장 긴 리스트 찾기
    if (len(biggerlst) < len(data_wordlst[i])) == True:
        bigger = len(data_wordlst[i])
        biggerlst = data_wordlst[i]
    else:
        bigger = len(biggerlst)
        biggerlst = biggerlst

for i in range(0,len(data_wordlst)):                    #위의 가장 긴 리스트를 제외 한 나머지 원소들을 같은 길이로 맞춤(내용은 None으로)
    if data_wordlst[i]==biggerlst:
        data_wordlst[i].append(0)


    else :
        for j in range(len(data_wordlst[i]),bigger):
            data_wordlst[i].append(None)
        data_wordlst[i].append(0)
print('dlst:',data_wordlst,'\n','dlst[len-1]',data_wordlst[len(data_wordlst)-1])
print(bigger)
for k in range(bigger+1):
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
disease.to_csv('./disease.csv', index=False, sep=',', na_rep='NaN', encoding='utf-8-sig')
print(disease)

