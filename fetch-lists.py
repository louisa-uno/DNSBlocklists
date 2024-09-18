import os
import shutil

import requests

from src.config.lists import categories

print(categories)
def clear_lists():
	for i in categories.keys():
		try:
			os.remove(i + ".txt")
		except FileNotFoundError:
			pass
		try:
			shutil.rmtree(i)
		except FileNotFoundError:
			pass

clear_lists()

list_file = ""
for category in categories.keys():
	try:
		os.mkdir(category)
	except FileExistsError:
		pass
	for i in categories[category]:
		response = requests.get(i["url"])
		with open(category + "/" + i["name"] + ".txt", "w", encoding="utf-8") as f:
			f.write(response.text)

full_list = ""
for category in categories.keys():
	category_list = ""
	for i in categories[category]:
		list = i["name"] + ".txt"
		with open(category + "/" + list, "r", encoding="utf-8") as f:
			category_list += f.read() + "\n"
	with open(category + ".txt", "w", encoding="utf-8") as f:
		f.write(category_list)
	full_list += category_list
with open("list" + ".txt", "w", encoding="utf-8") as f:
	f.write(full_list)