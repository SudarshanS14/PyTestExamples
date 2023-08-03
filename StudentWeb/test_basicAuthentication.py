import requests
from requests.auth import HTTPBasicAuth

def test_with_auth():
    response = requests.get("https://github.com/user",auth=HTTPBasicAuth('sudarshan147@gmail.com','gitHub123!'))
    print(response.text)