import os
import requests
import re

from joblib import Parallel, delayed

from src.config.lists import categories

def download_list(url, path):
	response = requests.get(url)
	with open(path, "w", encoding="utf-8") as f:
		if response.status_code != 200:
			print("Downloading returned status code: " + response.status_code + " for list: " + path)
		f.write(response.text)
   

downloads_list = []
for category in categories.keys():
	try:
		os.mkdir(category)
	except FileExistsError:
		pass
	for i in categories[category]:
		downloads_list.append([i["url"], category + "/" + i["name"] + ".txt"])

Parallel(n_jobs=16)(delayed(download_list)(i[0], i[1]) for i in downloads_list)


with open("allowlist.txt", "r", encoding="utf-8") as f:
	ALLOWLIST = f.read().splitlines()

def convert_pihole_list(list):
	pihole_list = []
	for line in list:
		line = line.replace("^", "")
		if "||" in line and not "*" in line and not "@@" in line:
			line = line.replace("||", "")
			if "|" in line:
				continue
			pihole_list.append(line)
	return pihole_list


def convert_line(line):
	# if any(x in line for x in ALLOWLIST):
	# return ""
	line = line.replace("0.0.0.0 ", "").replace("127.0.0.1 ", "")
	line = line.replace("^", "")
	line = line.split("$")[0]
	line += "^"
	if line.startswith("||") or line.startswith("@@"):
		return line
	else:
		return "||" + line


def skip_line(line):
	line = line.replace("||", "").replace("@@", "").replace("^", "")
	if any(x in line for x in ALLOWLIST):
		return True
	if line == "":
		return True
	forbidden_symbols = [" ", "#", "!", "/", "$"]
	if any(x in line for x in forbidden_symbols):
		return True
	return False


def is_valid_string(line):
	s = line.replace("|", "").replace("@@", "").replace("*", "").replace("^", "")
	return re.fullmatch(r'^[-.\w]+$', s) is not None


def convert_list(path):
	try:
		with open(path, "r", encoding="utf-8") as f:
			list = []
			for line in f.read().splitlines():
				line = convert_line(line)
				if skip_line(line):
					continue
				if not is_valid_string(line):
					print(line)
				list.append(line)
	except FileNotFoundError:
		print(f"File not found: {path}")
		return []
	return list


def write_lists_to_file(filtered_out, adguard_out, pihole_out, path):
	with open(path + ".txt", "w", encoding="utf-8") as f:
		f.write("\n".join(filtered_out))

	with open(path + ".adguard", "w", encoding="utf-8") as f:
		f.write("\n".join(adguard_out))

	with open(path + ".pihole", "w", encoding="utf-8") as f:
		f.write("\n".join(pihole_out))


adguard_list = []
pihole_list = []
for category in categories.keys():
	adguard_category_list = []
	pihole_category_list = []
	for i in categories[category]:
		converted_list = convert_list(i["txt"])
		adguard_category_list += converted_list
		pihole_category_list += convert_pihole_list(converted_list)
	write_lists_to_file(pihole_category_list, adguard_category_list, pihole_category_list, category)
	adguard_list += adguard_category_list
	pihole_list += pihole_category_list
write_lists_to_file(pihole_list, adguard_list, pihole_list, "list")
