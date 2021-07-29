import json
import requests
data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
ExtractedData = data.json()
articles = ExtractedData["articles"]

letter = "s"
for n in articles:
    name = n["author"]
    count={}.fromkeys(letter,0)
    print(name)
    for x in name.lower():
        if x in count:
            count[x] = count[x]+1

    print(count)

    