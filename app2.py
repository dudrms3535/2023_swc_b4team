from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta
# HTML을 주는 부분
@app.route('/')
def home():


return render_template('index.html')


# API 역할을 하는 부분(리뷰 부분 변경)
@app.route('/review', methods=['POST'])
def write_review():

# title_receive로 클라이언트가 준 title 가져오기
title_receive = request.form['title_give']
# author_receive로 클라이언트가 준 author 가져오기
author_receive = request.form['author_give']
# review_receive로 클라이언트가 준 review 가져오기
review_receive = request.form['review_give']
doc = {
'title': title_receive,
'author': author_receive,
'review': review_receive
}
# reviews에 review 저장하기
#db.bookreview.insert_one(doc)
# 성공 여부 & 성공 메시지 반환
#return jsonify({'msg': '리뷰가 성공적으로 작성되었습니다.'})

sample_receive = request.form['sample_give']
print(sample_receive)
return jsonify({'msg': '이 요청은 POST!'})













# 리뷰부분 변경
@app.route('/review', methods=['GET'])
def read_reviews():


sample_receive = request.args.get('sample_give')
print(sample_receive)
return jsonify({'msg': '이 요청은 GET!'})
if __name__ == '__main__':
app.run('0.0.0.0', port=5000, debug=True)











