from urllib.request import urlopen
from bs4 import BeautifulSoup
#모야모야병
html = urlopen("https://terms.naver.com/entry.naver?docId=926907&cid=51007&categoryId=51007")#서울대학교병원 의학정보
bsObject = BeautifulSoup(html, "html.parser")

for link1 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT3"}):
    print(link1) #증상
for link2 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT4"}):
    print(link2) #원인

symptomI= str(bsObject).index(str(link1)) #증상인덱스 변수값 할당
causationI= str(bsObject).index(str(link2)) #원인인덱스 변수값 할당
a=[]
for i in range(symptomI,causationI):
    #print(str(bsObject)[i],end='')
    a.append(str(bsObject)[i])

html = urlopen(
    "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810512&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EB%AA%A8%EC%95%BC%EB%AA%A8%EC%95%BC&schSort=kcdCd&schOrder=desc"
)# 질병 관리청 헬프라인
bsObject = BeautifulSoup(html, "html.parser")
print(link1) #증상
for link1 in bsObject.select('#detail02'):
    a.append(str(link1))

with open("C:/Users/hw499/PycharmProjects/CapstoneDesign/ SymptomFile/MoyaMoya.txt", "w", encoding='UTF=8') as symptomIFile:
    for text in a:
        symptomIFile.write(text)
