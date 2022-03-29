#Main.py
#coding: utf-8
from Connect import *
from ElementControl import *
from Parsing import *
from DBConnect import *
from Parsing import R_name_list

if __name__ == "__main__" :    

    p = Parsing()
    page = 1
    PageInURL = dict()
    #카테고리 별 URL 속 맛집 URL 수집
    while(page < 11):
        hotlinklist = []
        connectPageURL = PageURL(page)
        hotlinklist.append(p.getHotLink())
        PageInURL[page] = hotlinklist
        page += 1

    
    #맛집 정보 파싱
    for page in PageInURL.keys():
        for urllist in PageInURL[page]:
            for url in urllist:
                try:
                    info=p.parsingHot(url)
                    info['pageN'] = page
                    insertDB(info)
                except:
                    print("Parsing Error")
                    continue
