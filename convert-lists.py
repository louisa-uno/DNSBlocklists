import os

with open("allowlist.txt", "r", encoding="utf-8") as f:
	ALLOWLIST = []
	for line in f.readlines():
		ALLOWLIST.append(line.replace("\n", ""))


def convertList(path):
	if not ".txt" in path:
		return
	if "allowlist.txt" in path:
		return
	if ".adguard" in path or ".pihole" in path:
		return
	with open(path, "r", encoding="utf-8") as f:
		filteredOut, adguardOut, piholeOut = "", "", ""
		for line in f.readlines():
			forbiddenSubstrings = ["<", "! ", "  ", "!--"]
			if any(x in line for x in forbiddenSubstrings):
				continue
			if any(x in line for x in ALLOWLIST):
				continue
			commentSubstrings = ["# ", " #"]
			if any(x in line for x in commentSubstrings):
				line = line.split("#")[0].replace(" ", "") + "\n"
			if line == "\n":
				continue
			line = line.replace("0.0.0.0 ", "").replace("127.0.0.1 ", "")
			filteredOut += line
			adguardLine = line
			adguardOut += adguardLine
			if "!+ " not in line:
				piholeLine = line
				piholeLine = piholeLine.split("^")[0]
				piholeLine = piholeLine.replace("||", "")
				piholeOut += piholeLine
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
