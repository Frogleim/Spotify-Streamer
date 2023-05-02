# Spotify Streamer 

Spotify streamer for 24/7 streaming also included accounts generation

## Requirements 

```sh
Python 3.8 or upper
```

## Installation 

- create `users` directory for storing generated accounts data 
- install necessary libraries with command `pip install -r requirements.txt`  
- run `uvicorn` server with using `uvicorn main:app --reload`

## Endpoints

### Create Account
`api/create_account`

Currently there are available  only `create_account` endpoint, which generate `spotify` accounts with fake email address  





![Screenshot (9)](https://user-images.githubusercontent.com/92037197/235632304-22bfd821-ffa0-4902-85be-f636dd030844.png)


### Streaming 

For run `Spotify` streaming simply run `stream.py` , but don't forget to generate random account and put your playlist json 
in the main directory 