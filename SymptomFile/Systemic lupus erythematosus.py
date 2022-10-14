from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
dir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
a=[]
#전신홍반루푸스
html = urlopen("https://terms.naver.com/entry.naver?docId=926626&cid=51007&categoryId=51007") #서울대학교병원 의학정보
bsObject = BeautifulSoup(html, "html.parser")

for link1 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT3"}):
    print(link1) #증상
for link2 in bsObject.find_all('h3',{"id":"TABLE_OF_CONTENT4"}):
    print(link2) #진단/검사

symptomI= str(bsObject).index(str(link1)) #증상인덱스 변수값 할당
causationI= str(bsObject).index(str(link2)) #원인인덱스 변수값 할당

for i in range(symptomI,causationI):
    #print(str(bsObject)[i],end='')
    a.append(str(bsObject)[i])
print(link1) #증상

html = urlopen(
    "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810009&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EB%A3%A8%ED%91%B8%EC%8A%A4&schSort=kcdCd&schOrder=desc"
)# 질병 관리청 헬프라인
bsObject = BeautifulSoup(html, "html.parser")
for link4 in bsObject.select('div.contents table.dic_viewT tbody'):
    for i in range(str(link4.text).index('증상'),str(link4.text).index('원인')):#증상부터 원인앞의 인덱스를 이용하여 표의 증상 부분 크롤링
        # print("print",str(link4.text)[i])
        a.append(str(link4.text)[i])


print(a)
with open(dir+"/Systemic lupus erythematosus.txt", "w", encoding='UTF=8') as symptomIFile:
    for text in a:
        symptomIFile.write(text)
