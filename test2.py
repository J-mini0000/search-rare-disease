from konlpy.tag import Kkma
kkma = Kkma()	# 아마 설치가 잘 되지 않았다면 이 단계에서 에러가 났을 것이다.
print(kkma.nouns(u'안녕하세요 Soo입니다'))