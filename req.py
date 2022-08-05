import requests
import json
def api():
    url=requests.get("http://saral.navgurukul.org/api/courses")
    with open("courses.json","w")as file:
        dict=json.loads(url.text)
        json.dump(dict,file,indent=4)
        print(dict)
api()
