import requests
import json
import jsonpath


def test_add_student_data():
    api_url="https://thetestingworldapi.com/api/studentsDetails"    #Post link is POST api/studentsDetails so we give absolute path
    file_name=open("C:/scriptExample/Pytest/StudentWeb/request.json","r")
    json_request=json.loads(file_name.read())
    json_response=requests.post(api_url,json_request)
    print(f"Post update is ---- {json_response.text} \n")


def test_get_student_data():
    #GET api/studentsDetails/{id}
    api_url = "https://thetestingworldapi.com/api/studentsDetails/7695131"  # Post link is POST api/studentsDetails so we give absolute path with {ID}
    response=requests.get(api_url)
    print(f"Get update is ---- {response.text} \n")
    json_response = json.loads(response.text)   # or we can write json_response=response.json()
    id=jsonpath.jsonpath(json_response,'data.id')     #jsonpath always return list so we can assess using data.id.
    print(f" \n ID is {id} \n")
    assert id[0]==7695131

def test_update_student_data():
    api_url="https://thetestingworldapi.com/api/studentsDetails/7695131"    #Post link is POST api/studentsDetails so we give absolute path
    file_name=open("C:/scriptExample/Pytest/StudentWeb/request.json","r")
    json_request=json.loads(file_name.read())
    json_response=requests.put(api_url,json_request)
    print(f"JSON response is \n {json_response}")
    print(f"PUT update is ---- {json_response.text} \n")

def test_delete_student_data():
    api_url="https://thetestingworldapi.com/api/studentsDetails/7695131"
    response=requests.delete(api_url)
    print(f"Deleted {response.text}")
