import random
from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient('mongodb://localhost:27017')
db = client['flaskmongodb']
collection = db['Users']

# Kullanıcı verilerini oluştur ve ekle
for _ in range(50):
    name = random.choice(['Ahmet', 'Elif', 'İrem', 'Emily'])
    age = random.randint(0, 50)
    job = random.choice(['Engineer', 'Teacher', 'Doctor', 'Artist'])
    description = "1"
    
    user_data = {
        'Name': name,
        'Age': age,
        'Job': job,
        'Description': description
    }
    
    collection.insert_one(user_data)

print("Veri ekleme tamamlandı.")