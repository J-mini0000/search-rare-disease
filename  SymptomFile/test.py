from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://terms.naver.com/entry.naver?docId=2354118&cid=51362&categoryId=51362"
               )
bsObject = BeautifulSoup(html, "html.parser")

for link1 in bsObject.select('#TABLE_OF_CONTENT2'):
    print(link1) #증상
a=[]
a.append(str(link1))

with open("test.txt", "w", encoding='UTF=8') as symptomIFile:
    for text in a:
        symptomIFile.write(str(text))
