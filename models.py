from pymongo import MongoClient

client = MongoClient()
db = client['SalusMind']

def get_all_users():
    return db.users.find({'isConfirmed': True, 'isSuspended': False})

