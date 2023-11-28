import json

f = open('gameIds.json')

w = open("gameIdList", "w")
wJson = open("gameIdList.json", "w")

data = json.load(f)
f.close()

newIds = []

for idx, val in enumerate(data):
    if idx == 0:
        continue
    newIds.append(val['id'])
    w.write(val['id'])
    if idx != len(data) - 1:
        w.write(",")

w.close()

wJson.write(json.dumps(newIds))
