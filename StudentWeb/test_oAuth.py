import json
import requests
import jsonpath

def test_oAuth_api():
    token_url="https://thetestingworldapi.com/Token"
    data={'grant_type':'password','username':'admin','password':'adminpass'}
    response=requests.post(token_url,data)
    print(response.text)
    token_value=jsonpath.jsonpath(response.json(),'access_token')
    print(f"Token is  {token_value[0]}")

    auth={'Authorization':'Bearer'+token_value[0]}
    url="https://thetestingworldapi.com/api/StDetails/7696164"
    response=requests.get(url,headers=auth)
    print(response.text)
