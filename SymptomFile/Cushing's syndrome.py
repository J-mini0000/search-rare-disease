from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
dir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
#쿠싱증후군
html = urlopen("https://terms.naver.com/entry.naver?docId=6043716&cid=51362&categoryId=51362") #희귀질환정보
bsObject = BeautifulSoup(html, "html.parser")

#for link in bsObject.find_all('h3'):
#    print(link.text.strip(), link.get('href'))
#print(bsObject) #html코드 싹 가져오기
for link1 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT2"}):
    print(link1) #증상
for link2 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT3"}):
    print(link2) #원인

#증상이후부터 원인 이전까지만 긁어오고 싶습니다.
#print(str(bsObject).index(str(link1)))#증상인덱스찾기
#print(str(bsObject).index(str(link2)))#원인인덱스찾기

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
    "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810086&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EC%BF%A0%EC%8B%B1&schSort=kcdCd&schOrder=desc"
)# 질병 관리청 헬프라인
bsObject = BeautifulSoup(html, "html.parser")
print(link1) #증상
for link1 in bsObject.select('#detail02'):
    a.append(str(link1))

with open(dir+"/Cushing's syndrome symptomIFile.txt", "w", encoding='UTF=8') as symptomIFile:
    for text in a:
        symptomIFile.write(text)


