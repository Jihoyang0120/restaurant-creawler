from selenium import webdriver
# 장소 받기
print("핫 플레이스 검색: ")
place = input()
url = 'https://www.mangoplate.com/search/' + place

#ChromeDriver로 접속, 자원 로딩시간 3초
try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome('C:\chromedriver', options=options)
    driver.implicitly_wait(3)
    driver.refresh()
except: print("크롬드라이버 연결 에러")


#웹페이지 불러오기
def initpage():
    driver.get(url)

#레스토랑 서칭
def hConnect(url):
    driver.get('https://www.mangoplate.com/' + url)


#해쉬태그 서칭
def connect(n):
    driver.get(f'https://www.mangoplate.com/search/{place}?keyword=&page='+ str(n))
