# Spotify Streamer 

Spotify streamer for 24/7 streaming also included accounts generation

## Requirements 

```sh
Python 3.10.9
Selenium 4.12
```

## Installation 

- Download PostgresSQL from https://www.postgresql.org/download/
- install pgAdmin and set up admin password `0000`
- open pgAdmin and create database and set up database name as `spotify_accounts`
- install necessary libraries with command `pip install -r requirements.txt`  
- Enter your playlist url into `stream.py`



### Create Account
Run `python create_account.py`. It will create 2 accounts per 10 minutes


### Streaming 

For run `Spotify` streaming simply run `stream.py` 