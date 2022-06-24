import json
import os
import shutil

import requests

lists = json.load(open("lists.json"))

for f in os.listdir():
	if f == "allowlist.txt":
		continue
	if ".txt" in f:
		os.remove(f)
	if "." not in f:
		shutil.rmtree(f)

list_file = ""
for list in range(0, len(lists)):
	try:
		os.mkdir(lists[list]["category"])
	except FileExistsError:
		pass
	response = requests.get(lists[list]["url"])
	with open(lists[list]["category"] + "/" + lists[list]["name"] + ".txt",
	          "w",
	          encoding="utf-8") as f:
		f.write(response.text)

full_list = ""
for category in os.listdir():
	if category == ".git" or category == ".github" or "." in category:
		continue
	category_list = ""
	for list in os.listdir(category):
		with open(category + "/" + list, "r", encoding="utf-8") as f:
			category_list += f.read() + "\n"
	with open(category + ".txt", "w", encoding="utf-8") as f:
		f.write(category_list)
	full_list += category_list
with open("list" + ".txt", "w", encoding="utf-8") as f:
	f.write(full_list)
