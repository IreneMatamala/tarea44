from fastapi import FastAPI, HTTPException
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

app = FastAPI(title="DevSecOps Practice API")

# Configuración Azure Key Vault
KEY_VAULT_NAME = os.getenv("KEY_VAULT_NAME", "kv-devsecops")
KVUri = f"https://{KEY_VAULT_NAME}.vault.azure.net"

def get_secret_from_keyvault(secret_name: str) -> str:
   
    try:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)
        retrieved_secret = client.get_secret(secret_name)
        return retrieved_secret.value
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error accessing Key Vault: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "DevSecOps Practice API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/secret/{secret_name}")
def get_secret(secret_name: str):
  
    secret_value = get_secret_from_keyvault(secret_name)
    return {
        "secret_name": secret_name,
        "secret_value": "***" + secret_value[-4:] if secret_value else None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
