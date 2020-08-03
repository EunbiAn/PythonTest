import requests as r
from bs4 import BeautifulSoup

#웹 페이지의 데이터 가져오기

# response = r.get("http://www.danawa.com")
# get했을때 정보를 가져오지 못하는 페이지들이 있음

my_headers = {"User-agent" : "Mozilla/5.0"}
response = r.get("http://www.danawa.com", headers=my_headers)

# 가져온 데이터를 BeautifulSoup의 객체(인스턴스)로 만들기 (변환)
soup = BeautifulSoup(response.content, "html.parser")

# 자료를 제대로 가져왔는지 확인
# print(soup) #html 형태로 만들어짐

# <div class="main_middle_content"> 인 것을 찾아서 main 변수가 사용
main = soup.find( "div", {"class" : "main_middle_content"} )
# my_dict = { "key1":"value1", "key2":"value2" }
# print( main )
# 각각의 정보를 저장할 빈리스트 생성
data = []
product_index = 0

# <ul> 태그만 모두 찾아서 리스트화 하겠다.
for ul in main.find_all("ul"):
    # ul은 각각 하나의 <ul> 태그 내용들이 들어있다 (4개의 <ul> 태그 -> 4번 반복)
    for li in ul.find_all("li"):
        # li는 하나의 <ul>태그 안에서 8개의 <li> 태그를 하나씩 반복한다
        # <li> 태그 안에 하나의 제품 정보가 들어있다 (제품명, 가격)

        # print(li.text.strip().replace("\n"," ")) # <li> 태그 안의 text를 사용하겠다
        product_index += 1
        product = li.text.strip().replace("\n", " ").replace(",", "")
        data.append( [product_index, product] )

# 읽은 내용 파일로 저장하기
with open("danawa.csv","w") as file :
    # csv 파일은 comma seperated value (콤마로 구분된 값을 가진 파일)
    # csv는 엑셀에서 콤마 기준으로 한 셀씩 자동 분리해서 보여준다

    file.write("index,product\n") # 첫 째 줄은 제목용도로 사용할 것

    for i in data :
        file.write("{},{}\n".fomat(i[0], i[1])) #한 줄에 제품 하나씩