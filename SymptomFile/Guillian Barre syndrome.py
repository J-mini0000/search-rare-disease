from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
dir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
#길랭-바레증후군
html = urlopen("https://terms.naver.com/entry.naver?docId=926651&cid=51007&categoryId=51007") #서울대학교병원 의학정보
bsObject = BeautifulSoup(html, "html.parser")

for link1 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT3"}):
    print(link1) #증상
for link2 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT4"}):
    print(link2) #원인

# print(str(bsObject).index(str(link1)))#증상인덱스찾기
# print(str(bsObject).index(str(link2)))#원인인덱스찾기

symptomI= str(bsObject).index(str(link1)) #증상인덱스 변수값 할당
causationI= str(bsObject).index(str(link2)) #원인인덱스 변수값 할당
a=[]
for i in range(symptomI,causationI):
    #print(str(bsObject)[i],end='')
    a.append(str(bsObject)[i])


html = urlopen(
    "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810544&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=Guillain&schSort=kcdCd&schOrder=desc"
)# 질병 관리청 헬프라인
bsObject = BeautifulSoup(html, "html.parser")
print(link1) #증상
for link1 in bsObject.select('#detail02'):
    a.append(str(link1))


with open("./Guillian Barre syndrome.txt", "w", encoding='UTF=8') as symptomIFile:
    for text in a:
        symptomIFile.write(text)