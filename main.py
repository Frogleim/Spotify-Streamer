from fastapi import FastAPI
from change_password import change_password
from stream import start_streaming

app = FastAPI()


@app.get('/api/sing_up')
async def sign_up():
    final_data = change_password()
    return {'Message': final_data}


@app.get('/api/stream')
async def stream(message: str):
    if message:
        start_streaming()
        return {
            'Message': 'Streaming....'
        }
