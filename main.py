from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://dudrms3535:dudrms22@cluster0.ktigoqn.mongodb.net/test', tlsCAFile=ca)
db = client.sparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

# from selenium import webdriver




# 카카오 페이지 웹툰
# driver = webdriver.Chrome(executable_path="chromedriver")
# url = 'https://page.kakao.com/content/47686939?tab_type=about'
# driver.get(url)
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#
# kakao_main_soup1 = BeautifulSoup(driver.page_source, 'html.parser')
# kakao_mains1 = kakao_main_soup1.select('#__next > div > div.flex.w-full.grow.flex-col.px-122pxr')
# for kakao_main1 in kakao_mains1:
    # a = kakao_main1.select_one('div.flex.h-full.flex-1')
    # if a is not None:
        # kakao_image_give1 = kakao_main1.select_one('div.mb-28pxr.flex.w-320pxr.flex-col > div:nth-child(1) > div.w-320pxr.css-0 > div > div.css-0 > div.mx-auto.css-u4ybgy > div > div > img')['src']
        # kakao_title_give1 = kakao_main1.select_one(' div.mb-28pxr.flex.w-320pxr.flex-col > div:nth-child(1) > div.w-320pxr.css-0 > div > div.css-0 > div.relative.text-center.mx-32pxr.py-24pxr > span').text
        # kakao_author_give1 = kakao_main1.select_one('#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div.flex-1.bg-bg-a-20 > div:nth-child(1) > div.flex.flex-wrap.px-32pxr > a:nth-child(1) > button').text
        # kakao_genre_give1 = kakao_main1.select_one(' div.mb-28pxr.flex.w-320pxr.flex-col > div:nth-child(1) > div.w-320pxr.css-0 > div > div.css-0 > div.relative.text-center.mx-32pxr.py-24pxr > div.mt-16pxr.flex.items-center.justify-center.text-el-60.all-child\:font-small2 > span:nth-child(2)').text
        # kakao_summary_give1 = kakao_main1.select_one('div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div.flex-1.bg-bg-a-20 > div.text-el-60.break-keep.py-20pxr.pt-31pxr.pb-32pxr > span').text
        # doc = {
            # 'db_kakao_image_give1' : kakao_image_give1,
            # 'db_kakao_title_give1' : kakao_title_give1,
            # 'db_kakao_author_give1' : kakao_author_give1,
            # 'db_kakao_genre_give1' : kakao_genre_give1,
            # 'db_kakao_summary_give1' : kakao_summary_give1
        # }
        # db.kakaomain.insert_one(doc)



#
# naver_main_page = requests.get('https://comic.naver.com/webtoon/finish?order=ViewCount&view=image',headers=headers)
#
# naver_main_soup = BeautifulSoup(naver_main_page.text, 'html.parser')
# naver_mains = naver_main_soup.select('#content > div.list_area > ul > li')

# for naver_main in naver_mains:
    # a = naver_main.select_one('dl > dt > a')
    # if a is not None:
        # title_give = naver_main.select_one('dl > dt > a')['title']
        # views_give = naver_main.select_one('dl > dt > a')['onclick']
        # doc = {
            # 'main_title_give': title_give,
            # 'main_views_give': views_give
        # }
    # db.test2.insert_one(doc)



@app.route('/')
def home():
   return render_template('jemainpage.html')

@app.route("/main", methods=["GET"])
def naver_main_get():
    naver_main_sparta_api = list(db.kakaomain.find({}, {'_id':False}))
    return jsonify({'navers': naver_main_sparta_api})

@app.route("/thumbnail", methods=["GET"])
def naver_thumbnails_get():
    naver_main_sparta_api = list(db.naver_details.find({}, {'_id':False}))
    return jsonify({'thumbnails': naver_main_sparta_api})

@app.route("/toptoon", methods=["GET"])
def toptoon_thumbnails_get():
    toptoon_main_sparta_api = list(db.toptoonmain.find({}, {'_id':False}))
    return jsonify({'toptoons': toptoon_main_sparta_api})

@app.route("/detail", methods=["GET"])
def detail_NVComment_get():
    detail_NVComment_api = list(db.NVComment.find({}, {'_id':False}))
    return jsonify({'details1': detail_NVComment_api})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
Footer