from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://dudrms3535:dudrms22@cluster0.ktigoqn.mongodb.net/test', tlsCAFile=ca)
db = client.sparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

naver_main_page = requests.get('https://comic.naver.com/webtoon/finish?order=ViewCount&view=image',headers=headers)

naver_main_soup = BeautifulSoup(naver_main_page.text, 'html.parser')
naver_mains = naver_main_soup.select('#content > div.list_area > ul > li')

for naver_main in naver_mains:
    a = naver_main.select_one('dl > dt > a')
    if a is not None:
        title_give = naver_main.select_one('dl > dt > a')['title']
        views_give = naver_main.select_one('dl > dt > a')['onclick']
        doc = {
            'main_title_give': title_give,
            'main_views_give': views_give
        }
    db.test2.insert_one(doc)

@app.route('/')
def home():
   return render_template('jemainpage.html')

@app.route("/main", methods=["GET"])
def naver_main_get():
    naver_main_sparta_api = list(db.test2.find({}, {'_id':False}))
    return jsonify({'navers': naver_main_sparta_api})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
