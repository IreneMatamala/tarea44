from fastapi import FastAPI
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

app = FastAPI(title="DevSecOps Practice API")

# Azure Key Vault configuration
KEY_VAULT_NAME = os.getenv("KEY_VAULT_NAME", "kv-devsecops")
KVUri = f"https://{KEY_VAULT_NAME}.vault.azure.net"

@app.get("/")
async def read_root():
    return {"message": "DevSecOps Practice API is running!"}

@app.get("/secret/{secret_name}")
async def get_secret(secret_name: str):
    try:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)
        retrieved_secret = client.get_secret(secret_name)
        return {"secret_name": secret_name, "value": "***REDACTED***"}
    except Exception as e:
        return {"error": f"Failed to retrieve secret: {str(e)}"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
