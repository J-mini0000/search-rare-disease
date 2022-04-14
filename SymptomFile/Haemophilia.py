from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
dir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
#혈우병(제8인자 결핍증,제9인자 결핍증)
html = urlopen("https://terms.naver.com/entry.naver?docId=926705&cid=51007&categoryId=51007") #서울대학교병원 의학정보
bsObject = BeautifulSoup(html, "html.parser")

#for link in bsObject.find_all('h3'):
#    print(link.text.strip(), link.get('href'))
#print(bsObject) #html코드 싹 가져오기
for link1 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT2"}):
    print(link1) #증상
for link2 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT3"}):
    print(link2) #진단/검사

symptomI= str(bsObject).index(str(link1)) #증상인덱스 변수값 할당
causationI= str(bsObject).index(str(link2)) #원인인덱스 변수값 할당
a=[]
for i in range(symptomI,causationI):
    #print(str(bsObject)[i],end='')
    a.append(str(bsObject)[i])

html = urlopen("https://terms.naver.com/entry.naver?docId=926842&cid=51007&categoryId=51007") #서울대학교병원 의학정보
bsObject = BeautifulSoup(html, "html.parser")

for link1 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT3"}):
    print(link1) #증상
for link2 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT4"}):
    print(link2) #진단/검사

symptomI= str(bsObject).index(str(link1)) #증상인덱스 변수값 할당
causationI= str(bsObject).index(str(link2)) #진단/검사 인덱스 변수값 할당

for i in range(symptomI,causationI):
    #print(str(bsObject)[i],end='')
    a.append(str(bsObject)[i])

html = urlopen(
    "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810751&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=8%EC%9D%B8%EC%9E%90&schSort=kcdCd&schOrder=desc"
)# 질병 관리청 헬프라인
bsObject = BeautifulSoup(html, "html.parser")
print(link1) #증상
for link1 in bsObject.select('#detail02'):
    a.append(str(link1))

with open(dir+"/Haemophilia.txt", "w", encoding='UTF=8') as symptomIFile:
    for text in a:
        symptomIFile.write(text)
