import json
import requests
data = requests.get("https://jsonplaceholder.typicode.com/posts")
Extract=data.json()

userId= []
for i in Extract:
    userId.append(i["title"])
#print(title)
IdList = [c for c in userId if c[0]=="d" in c]
#Li.append(title)
print(IdList)