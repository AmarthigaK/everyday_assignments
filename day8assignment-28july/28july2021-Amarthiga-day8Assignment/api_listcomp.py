import json
import requests
data = requests.get("https://jsonplaceholder.typicode.com/posts")
Extract=data.json()
#x= Extract["data"]
#print(ExtractedData["article"])
#print(articles)
#print(data)

title= []
for i in Extract:
    title.append(i["title"])
#print(title)
Li = [c for c in title if c[0]=='a' in c]
#Li.append(title)
print(Li)




