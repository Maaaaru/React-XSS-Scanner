import os
from src.util.printer import colorized_print
from src.color import colors_list

exclude_dir = [".git", ".."]
target_file = [".js", ".jsx", ".ts", ".tsx"]
dangerous = ["javascript:", "dangerouslySetInnerHTML(", "eval("]

def scan_file(path):
	colorized_print("\n >> Scanning at " + path, colors_list.WHITE)

	with open(path) as f:
		for line_number, code in enumerate(f, 1):

			result = any(s in code for s in dangerous)

			scan_result(result, path, line_number)

def scan_dir(path):
	with os.scandir(path) as list:
		for item in list:
			if item.is_file() and os.path.splitext(item.name)[1] in target_file:
				scan_file(path+"/"+item.name)
			
			elif item.is_dir():
				if not item.name in exclude_dir:
					scan_dir(path+"/"+item.name)

def scan_result(is_denger, path, line):
	if (is_denger):
		colorized_print("\n  [ ! ] dangerous code found in " + path +  " at line " + str(line), colors_list.RED)
	else:
		colorized_print("\n  [ - ] dangerous code not found", colors_list.GREEN)
