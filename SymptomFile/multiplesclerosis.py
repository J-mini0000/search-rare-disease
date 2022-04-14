from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
#다발성 경화증
html = urlopen("https://terms.naver.com/entry.naver?docId=926680&cid=51007&categoryId=51007")#서울대학교병원 의학정보
bsObject = BeautifulSoup(html, "html.parser")

for link1 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT3"}):
    print(link1) #증상
for link2 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT4"}):
    print(link2) #원인

print(str(bsObject).index(str(link1)))#증상인덱스찾기
print(str(bsObject).index(str(link2)))#원인인덱스찾기

symptomI= str(bsObject).index(str(link1)) #증상인덱스 변수값 할당
causationI= str(bsObject).index(str(link2)) #원인인덱스 변수값 할당
a=[]
for i in range(symptomI,causationI):
    #print(str(bsObject)[i],end='')
    a.append(str(bsObject)[i])

html = urlopen(
    "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810551&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EB%8B%A4%EB%B0%9C%EA%B2%BD%ED%99%94%EC%A6%9D&schSort=kcdCd&schOrder=desc"
)# 질병 관리청 헬프라인
bsObject = BeautifulSoup(html, "html.parser")
print(link1) #증상
for link1 in bsObject.select('#detail02'):
    a.append(str(link1))

with open(dir+"/multiple sclerosis.txt", "w", encoding='UTF=8') as symptomIFile:

    for text in a:
        symptomIFile.write(text)