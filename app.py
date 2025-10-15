from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "¡App con Azure Key Vault!"

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/keyvault-test')
def keyvault_test():
    
    try:
        from azure.identity import DefaultAzureCredential
        from azure.keyvault.secrets import SecretClient
        
        credential = DefaultAzureCredential()
        client = SecretClient(
            vault_url="https://kv-tarea44.vault.azure.net", 
            credential=credential
        )
        
     
        secret = client.get_secret("db-connection")
        
        return jsonify({
            "keyvault_status": "CONECTADO",
            "secreto_obtenido": True,
            "longitud_secreto": len(secret.value),
            "mensaje": "¡Azure Key Vault funcionando!"
        })
        
    except Exception as e:
        return jsonify({
            "keyvault_status": "ERROR",
            "error": str(e),
            "solucion": "Ejecuta: az login"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
