import json

lists = json.load(open("lists.json"))

categories = {}
for i in lists:
	category = i["category"]
	if category not in categories:
		categories[category] = []
	categories[category].append({"name": i["name"], "url": i["url"], "txt": category + "/" + i["name"] + ".txt"})
# print(i)
# print(categories)
