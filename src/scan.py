import os
from src.util.printer import colorized_print
from src.color import colors_list

exclude_dir = [".git", ".."]
target_file = [".js", ".jsx",".ts",".tsx"]
dangerous = ["javascript:","dangerouslySetInnerHTML("]

def output_result(result, path):
	if (result):
		colorized_print("\n[ ! ] dangerous code found in " + path, colors_list.RED)
	else:
		colorized_print("[ - ] dangerous code not found", colors_list.GREEN)

def scan_file(path):
	with open(path) as f:
		for line in f:
			line = line.rstrip()
			result = any(s in line for s in dangerous)

			output_result(result, path)

def scan_dir(path):
	with os.scandir(path) as list:
		for item in list:
			if item.is_file() and os.path.splitext(item.name)[1] in target_file:
				scan_file(path+"/"+item.name)
			
			elif item.is_dir():
				if not item.name in exclude_dir:
					scan_dir(path+"/"+item.name)
