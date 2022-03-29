from Connect import place
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import string, random

# Use the application default credentials
cred = credentials.Certificate('C:\\dough-survey-firebase-adminsdk-e6t5s-b2c0127536.json')
firebase_admin.initialize_app(cred, {
  'projectId': 'dough-survey',
})

db = firestore.client()



def insertDB(dataDic):

    if '카테고리' in dataDic.keys():
        category = dataDic['카테고리']
    else:
        category = None
    
    if '이름' in dataDic.keys():
        R_name = dataDic['이름']
    else:
        R_name = None

    if '주소' in dataDic.keys():
        addr = dataDic['주소']
        x = addr.split(' ')
        R_gu = x[1]
        R_gil = x[2]
    else:
        addr = None
        R_gu = None
        R_gil = None

    if '전화번호' in dataDic.keys():
        tel = dataDic['전화번호']
    else:
        tel = None
    
    if '음식종류' in dataDic.keys():
        kind = dataDic['음식종류']
    else:
        kind = None
    
    if '평점' in dataDic.keys():
        rating = dataDic['평점']
    else:
        rating = None

    if '영업시간' in dataDic.keys():
        open_time = dataDic['영업시간']
    else:
        open_time = None

    if '휴일' in dataDic.keys():
        holiday = dataDic['휴일']
    else:
        holiday = None

    if '메뉴' in dataDic.keys():
        menu = dataDic['메뉴']
    else:
        menu = None
    # 키 세팅


    eatery_list = ["고기 요리", "국수 / 면 요리", "기타 한식", "기타 양식", "남미 음식", "라멘 / 소바 / 우동", "베이커리", "베트남 음식", "브런치 / 버거 / 샌드위치", "세계음식 기타", "스테이크 / 바베큐", "이탈리안", "인도 음식", "탕 / 찌개 / 전골", "태국 음식", "퓨전 양식", "프랑스 음식", "한정식 / 백반 / 정통 한식","해산물 요리"]
    cafe_list = ["카페 / 디저트", "베이커리"]
    try:
        if kind in cafe_list:
            category = "카페"
            # Place DB
            try:
                print("POST TO PLACE DB. Category is", category)
                doc_ref = db.collection(u"Place DB").document(R_name)
                # 키 생성
                key1 = random.choice(string.ascii_letters + string.digits)
                doc_ref.set({
                u'name': R_name,
                u'a_station':place,
                u'category':category,
                u'addr': addr,
                u'gu':R_gu,
                u'gil': R_gil,
                u'tel': tel,
                u'kind': kind,
                u'rating': rating,
                u'open_time':open_time,
                u'holiday':holiday,
                u'menu':menu,
                u'key':key1})
                print("매장 이름: {} 플레이스: {} 카테고리: {} 주소: {} 종류: {} 공유 키 값: {}".format(R_name, place, category, addr, kind, key1))
            except:
                print("PLACE DB ERROR")
            
            # Station DB
            try:
                print("POST TO STATION DB. Category is", category)
                doc_ref = db.collection(u"Station DB").document(place).collection(category).document(R_name)
                doc_ref.set({
                u'name': R_name,
                u'a_station':place,
                u'category':category,
                u'kind': kind,
                u'key':key1})
                print("매장 이름: {} 플레이스: {} 카테고리: {} 주소: {} 종류: {}".format(R_name, place, category, addr, kind, key1))
            except:
                print("STATION DB ERROR")
        
        elif category == place+"-술집" or category == place+"-치킨":
        
            try:
                print("POST TO STATION DB. Category is", category)
                doc_ref = db.collection(u"Place DB").document(R_name)
                # 키 생성
                key2 = random.choice(string.ascii_letters + string.digits)
                doc_ref.set({
                u'name': R_name,
                u'a_station':place,
                u'category':category,
                u'addr': addr,
                u'gu':R_gu,
                u'gil': R_gil,
                u'tel': tel,
                u'kind': kind,
                u'rating': rating,
                u'open_time':open_time,
                u'holiday':holiday,
                u'menu':menu,
                u'key':key2})
                print("매장 이름: {} 플레이스: {} 카테고리: {} 주소: {} 종류: {}".format(R_name, place, category, addr, kind, key2))
            except:
                print("PLACE DB ERROR")
            
            try:
                print("POST TO STATION DB. Category is", category)
                doc_ref = db.collection(u"Station DB").document(place).collection(category).document(R_name)
                doc_ref.set({
                u'name': R_name,
                u'a_station':place,
                u'category':category,
                u'kind': kind,
                u'key':key2})
                print("매장 이름: {} 플레이스: {} 카테고리: {} 주소: {} 종류: {}".format(R_name, place, category, addr, kind, key2))
            except:
                print("STATION DB ERROR")

    except:
        print("Connect Error")
