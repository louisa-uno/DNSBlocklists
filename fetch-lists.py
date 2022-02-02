import json
import os
import shutil

import requests
# from github import Github, InputGitAuthor

config = json.load(open("config.json"))
lists = json.load(open("lists.json"))

for f in os.listdir():
	if ".txt" in f:
		os.remove(f)
	if not "." in f:
		shutil.rmtree(f)

list_file = ""
for category in lists:
	category_file = ""
	os.mkdir(category)
	for list in lists[category]:
		response = requests.get(lists[category][list]["url"])
		with open(category + "/" + list + ".txt", "w", encoding="utf-8") as f:
			f.write(response.text)
		category_file += response.text + "\n"
	with open(category + ".txt", "w", encoding="utf-8") as f:
		f.write(category_file)
	list_file += category_file + "\n"
with open("list" + ".txt", "w", encoding="utf-8") as f:
	f.write(list_file)

# def push(path, message, content, branch):
# 	author = InputGitAuthor("Luois45 - Update lists", "github@louis45.de")
# 	contents = repo.get_contents(path, )
# 	repo.update_file(contents.path,
# 	                 message,
# 	                 content,
# 	                 contents.sha,
# 	                 branch=branch,
# 	                 author=author)

# repo = Github(
# 	    config["git_token"]).get_repo("Luois45/DNSBlocklists")
# 	push(path=".txt",
# 	     message="Updated DNS blocklists",
# 	     content=output,
# 	     branch="update")
# 	print("\nDNS blocklists to GitHub repository")