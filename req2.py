import requests
import json
url=requests.get("http://saral.navgurukul.org/api/courses")
with open("courses.json","w")as file:
    dict=json.loads(url.text)
    json.dump(dict,file,indent=4)
course=int(input("enter any course number:"))
if course in dict:
    print(dict,course) 
