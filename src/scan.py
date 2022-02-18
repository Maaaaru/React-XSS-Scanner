import os
from src.util.printer import colorized_print
from src.color import colors_list

exclude_dir = [".git", "..", "__test__",".github", "docs", ".bin", ".vscode", ".storybook", "dist"]
target_file = [".js", ".jsx", ".ts", ".tsx"]
dangerous = ["javascript:", "dangerouslySetInnerHTML(", "eval("]
vulnerable_files = []

def scan_file(path):
	vulnerable_code_line_number = []

	colorized_print("\n >> Scanning " + path, colors_list.WHITE)

	with open(path) as f:
		for line_number, code in enumerate(f, 1):

			result = any(s in code for s in dangerous)

			if result:
				vulnerable_code_line_number.append(line_number)

				colorized_print("\n  [ ! ] vulnerable code found", colors_list.RED)

	if (len(vulnerable_code_line_number) is 0):
		colorized_print("\n  [ - ] vulnerable code not found ", colors_list.GREEN)
	else:
		return vulnerable_files.append([path,vulnerable_code_line_number])

def is_target_file(file_name):
	return len(file_name.split(".")) is 2 and os.path.splitext(file_name)[1] in target_file

def scan_dir(path):
	with os.scandir(path) as list:
		for item in list:
			if item.is_file() and is_target_file(item.name):
				scan_file(path+"/"+item.name)
			
			elif item.is_dir():
				if not item.name in exclude_dir:
					scan_dir(path+"/"+item.name)
	return vulnerable_files
