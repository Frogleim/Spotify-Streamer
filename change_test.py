import time
import json
from stream import start_streaming


def start():
    users_file = open('./users/users.json')
    data = json.load(users_file)
    with open('song.txt', 'r') as f:
        mySongs = [line.strip() for line in f]
    for items in data['users']:
        start_streaming(
            email=items['email'],
            password=items['password'],
            playlist=mySongs[0]
        )


def radio():
    start_time = time.time()
    start()
    count = 0

    while True:
        time.sleep(1)
        count += 1
        users_file = open('./users/users.json')
        data = json.load(users_file)
        with open('song.txt', 'r') as f:
            mySongs = [line.strip() for line in f]
        for items in data['users']:
            start_streaming(
                email=items['email'],
                password=items['password'],
                playlist=mySongs[count]
            )
            time.sleep(2)
            if time.time() - start_time >= 60:
                time.sleep(90)


radio()
