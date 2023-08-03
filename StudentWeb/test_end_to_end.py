import requests
import json
import jsonpath

def test_Add_new_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f=open("C:/scriptExample/Pytest/StudentWeb/student.json","r")
    data=json.loads(f.read())
    print(f"data is --> {data} \n")
    response=requests.post(API_URL,data)
    print(f"Response is {response.text} \n")
    id=jsonpath.jsonpath(response.json(),'id')
    print(f"ID is {id[0]}")

    #Post technocal data https://thetestingworldapi.com/Help
    tech_url="https://thetestingworldapi.com/api/technicalskills"
    f = open("C:/scriptExample/Pytest/StudentWeb/postTechnical.json", "r")
    data=json.loads(f.read())
    data['id']=int(id[0])
    response=requests.post(tech_url,data)
    print(f"Technical data response is {response.text} \n")

    # Post address data
    address_url = "https://thetestingworldapi.com/api/addresses"
    f=open("C:/scriptExample/Pytest/StudentWeb/address.json", "r")
    data=json.loads(f.read())
    data['stId']=int(id[0])
    print(f"Address is {data} \n")
    response=requests.post(address_url,data)
    print(f"Address updated is {response.text} \n")

    #fetch complete student data
    student="https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response=requests.get(student)
    print(f"Student data is {response.text}")






    