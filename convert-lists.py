import re

from src.config.lists import categories

with open("allowlist.txt", "r", encoding="utf-8") as f:
	ALLOWLIST = []
	for line in f.readlines():
		ALLOWLIST.append(line.replace("\n", ""))
	print(ALLOWLIST)


def convert_pihole_list(list):
	pihole_list = []
	for line in list:
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
	if line.startswith("||") or line.startswith("@@"):
		return line
	else:
		return "||" + line


def skip_line(line):
	line = line.replace("||", "").replace("@@", "")
	if any(x in line for x in ALLOWLIST):
		return True
	if " " in line:
		return True
	if "#" in line or "!" in line:
		return True
	if line == "":
		return True
	if "/" in line:
		return True
	if "@@" in line:  # Unblock param
		return True
	if "$" in line:
		return True
	return False


def is_valid_string(line):
	s = line.replace("|", "").replace("@@", "").replace("*", "")
	return re.fullmatch(r'^[-.\w]+$', s) is not None


def convert_list(path):
	try:
		with open(path, "r", encoding="utf-8") as f:
			list = []
			for line in f.read().splitlines():
				line = convert_line(line)
				# Skip all allowlist entries
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
		adguard_category_list += convert_list(i["txt"])
		pihole_category_list += convert_pihole_list(convert_list(i["txt"]))
	write_lists_to_file(pihole_category_list, adguard_category_list, pihole_category_list, category)
	adguard_list += adguard_category_list
	pihole_list += pihole_category_list
write_lists_to_file(pihole_list, adguard_list, pihole_list, "list")
