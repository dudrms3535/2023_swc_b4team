from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://dudrms3535:<패스워드>@cluster0.ktigoqn.mongodb.net/test', tlsCAFile=ca)
db = client.sparta
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

#네이버 웹툰 메인페이지 용도
naver_main_page = requests.get('https://comic.naver.com/webtoon/finish?order=ViewCount&view=image',headers=headers)
#디테일 페이지는 주소가 매번 바뀌기에.. ㅠ 수동입력
naver_detail_page = requests.get('https://comic.naver.com/webtoon/list?titleId=729938',headers=headers)

naver_main_soup = BeautifulSoup(naver_main_page.text, 'html.parser')
naver_detail_soup = BeautifulSoup(naver_detail_page.text, 'html.parser')

naver_mains = naver_main_soup.select('#content > div.list_area > ul > li')
naver_details = naver_detail_soup.select('#content > div.comicinfo')

#카카오 웹툰 메인페이지 용도




# 네이버 웹툰 메인 페이지 크롤링 후 DB 저장
# for naver_main in naver_mains:
    # a = naver_main.select_one('dl > dt > a')
    # if a is not None:
        # title_give = naver_main.select_one('dl > dt > a')['title']
        # views_give = naver_main.select_one('dl > dt > a')['onclick']
        # doc = {
            # 'main_title_give' : title_give,
            # 'main_views_give' : views_give
        # }
        # db.sparta.insert_one(doc)

# 네이버 웹툰 디테일 페이지 크롤링 후 DB 저장
# for naver_detail in naver_details:
    # a = naver_detail.select_one('div.detail')
    # if a is not None:
        # title_give = naver_detail.select_one('h2 > span').text 
        # author_give = naver_detail.select('h2 > span.wrt_nm')[0].text.replace(" ","")
        # genre_give = naver_detail.select('p > span')[0].text
        # summary_give = naver_detail.select_one('p').text
        # doc = {
            # 'detail_title_give' : title_give,
            # 'detail_author_give' : author_give,
            # 'detail_genre_give' : genre_give,
            # 'detail_summary_give' : summary_give
        # }
        # db.detail.insert_one(doc)

# 메인 홈페이지 route API
@app.route('/')
def home():
    return render_template('index.html')


# 현재는 미사용 API
# @app.route("/bucket", methods=["POST"])
# def bucket_post():
    # bucket_receive = request.form['bucket_give']
    # doc = {
        # 'num':0,
        # 'bucket':bucket_receive,
        # 'done':0
    # }
    # db.bucket.insert_one(doc)
    # return jsonify({'msg': '등록 완료!'})

# 현재는 미사용 API
# @app.route("/bucket/done", methods=["POST"])
# def bucket_done():
    # sample_receive = request.form['sample_give']
    # print(sample_receive)
    # return jsonify({'msg': 'POST(완료) 연결 완료!'})

# 네이버 웹툰 메인페이지 GET API
@app.route("/main", methods=["GET"])
def naver_main_get():
    naver_main_sparta_api = list(db.sparta.find({}, {'_id':False}))
    return jsonify({'navers': naver_main_sparta_api})



# 필수 코드?
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
