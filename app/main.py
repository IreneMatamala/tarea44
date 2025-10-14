from fastapi import FastAPI, HTTPException
import os


app = FastAPI()


KV_NAME = os.getenv('KEYVAULT_NAME') # nombre del Key Vault, p.ej. kv-devsecops
SECRET_NAME = os.getenv('SECRET_NAME', 'db-connection')


@app.get('/health')
async def health():
return {'status': 'ok'}


@app.get('/secret')
async def get_secret():

if not KV_NAME:
raise HTTPException(status_code=500, detail='KEYVAULT_NAME not set')


try:
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


credential = DefaultAzureCredential()
kv_url = f"https://{KV_NAME}.vault.azure.net"
client = SecretClient(vault_url=kv_url, credential=credential)
secret = client.get_secret(SECRET_NAME)
return {'secret_name': SECRET_NAME, 'value': secret.value}
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))




if __name__ == '__main__':
import uvicorn
uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=False)
