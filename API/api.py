import requests

# Configuration
TOKEN_URL="https://auth-int.iam.telefonica.de/eiam/oauth2/access_token"


CLIENT_ID="	b0f25856-a63f-497c-bcb5-a6de30a8cf01"
CLIENT_SECRET="q7gvJuEh1O6UB5FNIqEEQDkPyJZX8D4m267Q0QpEBo5fxiV8n7KH_HpmsoB5UNc2DqNN_sphiO96UZw7Ntyplw"

def get_new_token():
    payload ={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    try:
        response = requests.post(TOKEN_URL,data=payload,timeout=5)
        response.raise_for_status()
        
        token=response.json().get("access_token")
        print("Token retrived successfully")
        
        return token

    except requests.exceptions.RequestException as e:
        print(f"Failed to get token: {e}")
        return None
    
    
if __name__=="__main__":
    get_new_token()
