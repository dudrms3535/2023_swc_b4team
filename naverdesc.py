import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import certifi
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

ca = certifi.where()
client = MongoClient('mongodb+srv://dudrms3535:dudrms22@cluster0.ktigoqn.mongodb.net/test', tlsCAFile=ca)
db = client.sparta

url = "https://comic.naver.com/webtoon/list?titleId=651673"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

naver_details = soup.find_all("div", class_="detail")

#for naver_detail in naver_details:
#    a = naver_detail.select_one('div.detail > h2 > span.title')
#    if a is not None:
#        title = a.text
#        author = naver_detail.select_one('div.detail > h2 > span.wrt_nm').text
#        main_thumb = naver_detail.select_one('div.thumb > a > img')['src']
#        topic = naver_detail.select_one('div.detail > p.detail_info > span.genre').text
#        summary = naver_detail.select_one('div.detail > p:nth-child(2)').text
        # print(title, author.lstrip(), main_thumb, topic, summary)

#        doc = {
#            'title': title,
#            'author': author,
#            'main_thumb': main_thumb,
#            'topic': topic,
#            'summary': summary
#        }

#       db.naver_details.insert_one(doc)

@app.route('/')
def home():
   return render_template('naverthumbnail.html')

@app.route("/main", methods=["GET"])
def naver_main_get():
    naver_main_sparta_api = list(db.naver_details.find({}, {'_id':False}))
    return jsonify({'navers': naver_main_sparta_api})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)