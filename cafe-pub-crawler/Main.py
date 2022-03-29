#Main.py
#coding: utf-8
from Connect import place
from Connect import *
from ElementControl import *
from Parsing import *
from DBConnect import *
from Parsing import R_name_list

if __name__ == "__main__" :    


    #해쉬태그
    hashTag = [place+"-카페",place+"-술집",place+"-치킨",place+"-이탈리안"]
    print(hashTag)

    #맛집리스트 웹 자원 활용 객체
    e = Toplist()
    print("Toplist loaded")
    #웹 페이지 파싱 객체
    p = Parsing()
    print("Parsing Done")

    #해쉬태그 리스트 수집 후 URL 변환
    collect = p.collectHashTag()
    
    
    #딕셔너리 형으로 카테고리 별 URL 분류
    category = dict()
    for index in range(0, len(hashTag)):
        category[hashTag[index]] = collect[index]

    categoryInURL = dict()
    print(category)

    #카테고리 별 URL 속 맛집 URL 수집
    for key in category.keys():
        hotlinklist = []
        connectCategoryURL = CategoryURL(key)
        hotlinklist.append(p.getHotLink())
        categoryInURL[key] = hotlinklist
    print(categoryInURL[key])
        

    
    #맛집 정보 파싱
    for key in categoryInURL.keys():
        for urllist in categoryInURL[key]:
            for url in urllist:
                try:
                    info=p.parsingHot(url)
                    info['카테고리'] = key
                    #print(str(info))
                    #if(info['주소'].find('서울특별시') != 1):
                    insertDB(info)
                except:
                    continue

