from fastapi import FastAPI
from change_password import run
# from stream import start_streaming
from create_account import Main

app = FastAPI()


@app.get('/api/create_account')
async def create_account():
    create_accounts = Main()
    res = create_accounts.run()
    return {
        "Accounts": res
    }


@app.get('/api/sing_up')
async def sign_up():
    final_data = run()
    return {'Message': final_data}


@app.get('/api/stream')
async def stream(message: str):
    if message:
        start_streaming()
        return {
            'Message': 'Streaming....'
        }
