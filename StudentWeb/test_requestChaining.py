#fetch student ID and use it to get last name.

import json
import jsonpath
import requests

def test_add_new_student():
    global id
    url="https://thetestingworldapi.com/api/studentsDetails"
    studentInfo=open("C:/scriptExample/Pytest/StudentWeb/addStudent.json","r")
    json_content=json.loads(studentInfo.read())
    response=requests.post(url,json_content)
    id=jsonpath.jsonpath(response.json(),'id')
    print(f"Response is {response.text} \n")
    print(f"ID is {id[0]} \n")


def test_get_details():
    print(f"ID is {id[0]} \n")
    url="https://thetestingworldapi.com/api/technicalskills/"+str(id[0])
    print(f"URL is  {url} \n")
    response=requests.get(url)
    print(response.text)



