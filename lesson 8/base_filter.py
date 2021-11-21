from pymongo import MongoClient
from pprint import pprint
client = MongoClient('localhost', 27017)
db = client['instagram_scrapy']
users = db.instagram

name = input('Укажите имя пользователя: ')
cnt = users.count_documents({'$and': [{'source_name': name, 'subs_type': 'subscriber'}]})
print(f'Подписчики {cnt}:')
for user in users.find({'$and': [{'source_name': name, 'subs_type': 'subscriber'}]}):
    pprint(user)
print('_____________________________________')
cnt = users.count_documents({'$and': [{'source_name': name, 'subs_type': 'subscription'}]})
print(f'Подписки {cnt}:')
for user in users.find({'$and': [{'source_name': name, 'subs_type': 'subscription'}]}):
    pprint(user)