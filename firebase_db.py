import firebase_admin
from firebase_admin import credentials, firestore
import json

cred = credentials.Certificate("./spotify-streamer-18cc3-firebase-adminsdk-us15t-2e400350e5.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
# collection = db.collection('spotify_users')
collection = db.collection('places')
print(collection)


def read_data():
    file = open(r'./users/client_credentials_final.json')
    data = json.load(file)
    return data


def store_data():
    data = read_data()
    documentID = 0
    for items in data['users']:
        documentID += 1
        collection.document(f'user_{str(documentID)}').set({
            'email': items['email'],
            'password': items['password']
        })
        print('Saved successful')


def get_data():
    docs = collection.get()
    count = 1
    for i in range(len(docs)):
        count += 1
        doc = collection.document(f'user_{str(count)}')
        res = doc.get().to_dict()
        print(res['email'])


other_songs = 1

song_file = open(r'./playlist.json')
songs = json.load(song_file)
for playlists in songs['playlist'][other_songs:other_songs + 1]:
    print(playlists)
#
# if __name__ == '__main__':
#     get_data()