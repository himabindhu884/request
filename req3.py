import requests
import json
from pprint import pprint

url=requests.get("http://saral.navgurukul.org/api/courses")
data=url.json()
def select(choose,var,data1,slug):
    a=var
    while True:
        print("Choose 'up' for go to up course")
        print("Choose 'next' for go to next course")
        print("Choose 'previous' for go to previous course")
        print("Choose 'exit' for exit")
        select=input("choose anyone in up,next,previous,exit:")
        if select=="up":
            pprint(a)
            a=var-1
            y=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"/exercise/getBySlug?slug="+str(slug[a-1]))
            z=y.json()
            print(z["content"])
            pprint(a)
        elif select=="next":
            a=a+1
            y1=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"/exercise/getBySlug?slug="+str(slug[a-1]))
            y2=y1.json()
            print(y2["content"])
            pprint(a)
        elif select=="previous":
            d=1
            for l in data1["data"]:
                print(d,l["name"])
                d+=1
        elif select=="exit":
            api()
def api():
    count=1
    for i in data["availableCourses"]:
        print(count,i["name"],":",i["id"])
        count+=1
    for j in data["availableCourses"]:
        a=int(input("enter any course:"))
        choose=data["availableCourses"][a-1]["id"]
        var=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"/exercises")
        data1=var.json()
        b=1
        slug=[]
        for k in data1["data"]:
            print(b,k["slug"])
            slug.append(k["slug"])
            b+=1
        c=int(input("select any slug:"))
        var1=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"/exercise/getBySlug?slug="+str(slug[c-1]))
        var2=var1.json()
        print(var2["content"])
        select(choose,c,data1,slug)
api()