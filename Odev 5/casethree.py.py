from flask import Flask, request, jsonify
from bson import ObjectId, json_util
from pymongo import MongoClient

# Flask uygulamasını başlat
app = Flask(__name__)
app.config['DEBUG'] = True  # Hata ayıklama modunu etkinleştir

# MongoDB'ye bağlan
client = MongoClient('mongodb://localhost:27017')
db = client['flaskmongodb']
collection = db['Users']

# Endpoint 1: Kullanıcı ekleme
@app.route('/adduser', methods=['POST'])
def add_user():
    user_data = request.json

    # Kullanıcıyı Users koleksiyonuna ekle
    inserted_user = collection.insert_one(user_data)

    return jsonify({'message': 'Kullanıcı başarıyla eklendi', 'id': str(inserted_user.inserted_id)})

# Endpoint 2: Yaşı 25'ten büyük olanları döndürme
@app.route('/25', methods=['GET'])
def get_users_above_25():
    filtered_users = collection.find({"age": {"$gt": 25}})
    users = []

    for user in filtered_users:
        users.append(user)

    return json_util.dumps(users)

# Endpoint 3: Tüm kullanıcıları döndürme
@app.route('/', methods=['GET'])
def get_all_users():
    all_users = collection.find()
    users = []

    for user in all_users:
        users.append(user)

    return json_util.dumps(users)

# Endpoint 4: Verilen id'ye sahip kullanıcıyı silme
@app.route('/deleteuser', methods=['POST', 'DELETE'])
def delete_user():
    user_id = request.json['id']

    # Kullanıcıyı id'ye göre sil
    collection.delete_one({"_id": ObjectId(user_id)})

    return jsonify({'message': 'Kullanıcı başarıyla silindi'})

# Flask uygulamasını çalıştırma
if __name__ == '__main__':
    app.run()
