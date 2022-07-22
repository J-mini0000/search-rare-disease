import csv
import pandas as pd
a=[]
final=[]
f = open('result.csv', 'r', encoding='utf-8-sig') #매칭시킨 결과 읽어오기
crd = csv.reader(f)
result = []
for exel in crd:
    result.append(exel)
f.close()

for i in range(0,len(result[0])):
    a.append([result[0][i],int(result[len(result)-1][i])]) #리스트 a에 [질환명, 카운트수] 형태로 저장.
    a.sort(key=lambda x: (-x[1]))  #리스트 a의 카운트수를 내림차순으로 sorting
# print(a)
# print(len(a))
final.append(["질환명","Count","질환정보"])
for i in range(0,4):
    final.append(a[i])              #리스트 a의 카운트수 상위 4질환을 리스트 final에 저장
    if (a[i][0] == "쿠싱증후군"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810086&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EC%BF%A0%EC%8B%B1&schSort=kcdCd&schOrder=desc")
    elif (a[i][0] == "크론병"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810504&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%ED%81%AC%EB%A1%A0%EB%B3%91&schSort=kcdCd&schOrder=desc")
    elif (a[i][0] == "다발성 경화증"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810551&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EB%8B%A4%EB%B0%9C%EA%B2%BD%ED%99%94%EC%A6%9D&schSort=kcdCd&schOrder=desc")
    elif (a[i][0] == "모야모야병"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810512&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EB%AA%A8%EC%95%BC%EB%AA%A8%EC%95%BC&schSort=kcdCd&schOrder=desc")
    elif (a[i][0] == "특발성 폐섬유화증"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810523&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%ED%8A%B9%EB%B0%9C%EC%84%B1+%ED%8F%90&schSort=kcdCd&schOrder=desc")
    elif (a[i][0] == "길렝-바레 증후군"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810544&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=Guillain&schSort=kcdCd&schOrder=desc")
    elif (a[i][0] == "혈우병(제 8,9인자 결함)"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810751&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=8%EC%9D%B8%EC%9E%90&schSort=kcdCd&schOrder=desc")
    elif (a[i][0] == "확장성 심근병증"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810514&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EC%8B%AC%EA%B7%BC%EB%B3%91%EC%A6%9D&schSort=kcdCd&schOrder=desc",
            "\nhttps://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810524&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EC%8B%AC%EA%B7%BC%EB%B3%91%EC%A6%9D&schSort=kcdCd&schOrder=desc",
            "\nhttps://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810516&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EC%8B%AC%EA%B7%BC%EB%B3%91%EC%A6%9D&schSort=kcdCd&schOrder=desc")
    elif (a[i][0] == "전신홍반루푸스"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810009&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EB%A3%A8%ED%91%B8%EC%8A%A4&schSort=kcdCd&schOrder=desc")
    elif (a[i][0] == "중증근무력증"):
        a[i].append(
            "https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=RA201810623&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=%EC%A4%91%EC%A6%9D%EA%B7%BC%EB%AC%B4%EB%A0%A5%EC%A6%9D&schSort=kcdCd&schOrder=desc")
    else:
        a[i].append(None)
print(final)
final=pd.DataFrame(final)                                   #리스트 final을 데이터프레임 형태로 변환
final.to_csv('./final.csv', index= False, sep=',', na_rep='NaN',header=None, encoding='utf-8-sig')
print("final: ", final)