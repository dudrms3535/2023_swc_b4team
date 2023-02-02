from pymongo import MongoClient
import certifi

ca = certifi.where()


client = MongoClient('mongodb+srv://dudrms3535:dudrms22@cluster0.ktigoqn.mongodb.net/test', tlsCAFile=ca)
db = client.sparta


doc = {
    'name' : 'bob',
    'age' : 27

}

db.users.insert_one(doc)