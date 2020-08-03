# wheatherCrawling.cy
# 2020.07.31
# 네이버 날씨 웹 크롤링하여 원하는 데이터 추출

from bs4 import BeautifulSoup
from pprint import pprint       #pprint는 딕셔너리의 데이터가 긴 경우에는 좀 더 보기 편하게 도와줌
import requests

html = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8')
# 웹페이지 요청을 하는 코드
# 특정 url을 적으면 웹페이지의 소스코드를 볼 수 있음

#pprint(html.text) # html이라는 변수에 저장된 소스코드 중 pprint로 정렬한 것

soup = BeautifulSoup(html.text, 'html.parser')
# 파이썬에서 보기 좋게, 다루기 쉽게 파싱작업을 거쳐야 각 요소에 접근이 쉬워진다

data1 = soup.find('div', {'class':'weather_box'})
# soup 모듈의 find 함수를 사용하여 data1에 값을 저장함
# 매개변수에는 div 태그명과 class라는 속성의 값이 weather_box라는 것을 딕셔너리로 저장
# find 함수를 사용할 때 주의할 점은 같은 웹페이지 소스코드에 같은 소스가 여러가지 있으면 맨 처음 탐색된덕만 반환하고 나머지는 무시

#weather_box 내부에 있는 정보들 중 현재 주소 추출
find_address = data1.find('span',{'class':'btn_select'}).text
print('현재 위치: '+find_address)
# data1 변수에 저장된 정보중 sapn 태그명과 btn_select라는 속성값을 갖고 있는 것을 딕셔너리로 저장

#온도정보 추출
find_currenttemp = data1.find('span',{'class':'todaytemp'}).text
print('현재온도: '+find_currenttemp+'C')


# 미세먼지, 초미세먼지, 오존지수 추출
# 각 줄이 dd라는 공통 태그를 갖고 있으며 클래스 명이 지수에 따라 계속 변화됨
# find는 첫 정보만 반환하므로 findAll함수 사용
data2 = data1.findAll('dd')

find_dust = data2[0].find('span',{'class':'num'}).text
find_ultra_dust = data2[1].find('span', {'class':'num'}).text
find_ozone = data2[2].find('span',{'class':'num'}).text
print('현재 미세먼지: '+find_dust)
print('현재 초미세먼지: '+find_ultra_dust)
print('현재 오존지수: '+find_ozone)


'''
출처 : https://velog.io/@magnoliarfsit/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-2-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%82%A0%EC%94%A8-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EA%B8%B0
를 보고 작성한 코드입니다
'''

























