# Spotify Streamer 

Spotify streamer for 24/7 streaming also included accounts generation

## Requirements 

```sh
Python 3.8 or upper
```

## Installation 

- create `PostgresSQL` db and input your db credentials into `/core/postgres_connect.py` 
- install necessary libraries with command `pip install -r requirements.txt`  
- Enter your playlist url into `stream.py`



### Create Account
Run `python create_account.py`. It will create 2 accounts per 10 minutes


### Streaming 

For run `Spotify` streaming simply run `stream.py` 