#Parsing.py
from Connect import *
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep

# 맛집 이름 리스트 생성
R_name_list = []
def hConnect(url): 
    driver.get('https://www.mangoplate.com' + url)

class Parsing :

    
    #지하철역 주변 맛집 해쉬태그 수집
    def collectHashTag(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        collect = []
        i = 0
        while(i < 11):
            for dataKeyWord in soup.find_all('a',{'class': 'region_by_keyword'}):
                if dataKeyWord.get('href') is None:
                    continue
                else:
                    collect.append(urljoin('https://www.mangoplate.com/',dataKeyWord.get('href')))
                    i += 1
        return collect

    """
    #지하철역 주변 맛집 해쉬태그 링크 수집
    def getLink(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        rlink = []
        for link in soup.find_all('a'):
            try:
                if link.get('href').find('serch/') != -1 :
                    rlink.append(link.get('href'))
            except AttributeError:
                continue
        return rlink
    """

    #지하철역 주변 맛집 URL 수집
    def getHotLink(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        hotlink = []
        for link in soup.find_all('a'):
            try:
                if link.get('href').find('restaurants') != -1 :
                    if link.get('href').find('restaurant_key') == -1 :
                        hotlink.append(link.get('href'))
            except AttributeError:
                continue
        return list(set(hotlink))

    #수집한 맛집 정보 파싱, 전처리
    def parsingHot(self, url):
        hConnect(url)
        driver.implicitly_wait(3)
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        #맛집 이름
        title = soup.find("h1",{"class": "restaurant_name"})
        #맛집 평점
        rating = soup.find("strong",{"class": "rate-point"})
        #맛집 정보
        info = dict()
        info['이름'] = title.get_text()
        #맛집 이름 추가
        R_name_list.append(title.get_text())
        print(R_name_list)
        info['평점'] = rating.get_text().replace('\n', '')
        table = soup.find("tbody")
        for thtd in table.find_all("tr"):
            if thtd.th.get_text() != "메뉴":
                temp = thtd.th.get_text().replace(' ', '')
                info[temp.replace('\n', '')] = thtd.td.get_text().replace('\n', '')
            else:
                info[thtd.th.get_text()] = thtd.td.get_text()
        return info
        #except AttributeError:
        #    print("없음")
