import requests, json, os, urllib.request

with urllib.request.urlopen("http://labs.bible.org/api/?passage=votd&type=json") as url:
    data = json.loads(url.read().decode())
    print(data[0]["bookname"] + " " + data[0]["chapter"] + ":" + data[0]["verse"] + " " + data[0]["text"])



book = data[0]["bookname"]
chapter = data[0]["chapter"]
verse = data[0]["verse"]
text = data[0]["text"]


post = book + " " + chapter + ":" + verse + " " + '\n' + text
data = { 'bot_id' : '43db4c5290a3c0996f7220df31',
         'text': post }
requests.post('https://api.groupme.com/v3/bots/post',
              params = data)