import os

with open("allowlist.txt", "r", encoding="utf-8") as f:
	ALLOWLIST = []
	for line in f.readlines():
		ALLOWLIST.append(line.replace("\n", ""))


def checkIfValidFile(path):
	if not ".txt" in path:
		return False
	if "allowlist.txt" in path:
		return False
	if ".adguard" in path or ".pihole" in path:
		return False
	return True


def convertLine(line):
	if any(x in line for x in ALLOWLIST):
		return ""
	line = line.replace("0.0.0.0 ", "").replace("127.0.0.1 ", "")
	commentSubstrings = ["# ", " #"]
	if any(x in line for x in commentSubstrings):
		line = line.split("#")[0].replace(" ", "") + "\n"
	return line


def convertAdguardLine(line):
	return line


def convertPiholeLine(line):
	if any(x in line for x in ["/", "*", "$", "!", "<", ">"]):
		return ""
	line = line.replace("||", "")
	if "^" in line:
		line = line.split("^")[0] + "\n"
	if "#[" in line:
		line = line.replace("#[", "").replace("]", "")
	return line


def convertList(path):
	if checkIfValidFile(path) is False:
		return
	with open(path, "r", encoding="utf-8") as f:
		filteredOut, adguardOut, piholeOut = "", "", ""
		for line in f.readlines():
			line = convertLine(line)
			filteredOut += line
			adguardOut += convertAdguardLine(line)
			piholeOut += convertPiholeLine(line)
	with open(path, "w", encoding="utf-8") as f:
		f.write(filteredOut)
	with open(path.replace(".txt", ".adguard"), "w", encoding="utf-8") as f:
		f.write(adguardOut)
	with open(path.replace(".txt", ".pihole"), "w", encoding="utf-8") as f:
		f.write(piholeOut)


for category in os.listdir():
	if category == ".git" or category == ".github" in category:
		continue
	try:
		for list in os.listdir(category):
			convertList(category + "/" + list)
	except NotADirectoryError:
		convertList(category)
