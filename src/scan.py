import os
from src.util.printer import colorized_print
from src.color import colors_list

exclude_dir = [".git", "..", "__test__",".github", "docs", ".bin", ".vscode", ".storybook"]
target_file = [".js", ".jsx", ".ts", ".tsx"]
dangerous = ["javascript:", "dangerouslySetInnerHTML(", "eval("]
num_of_dangerous_code = 0

def scan_file(path):

	colorized_print("\n >> Scanning at " + path, colors_list.WHITE)

	with open(path) as f:
		for line_number, code in enumerate(f, 1):

			result = any(s in code for s in dangerous)

			if result:
				num_of_dangerous_code + 1

			scan_result(result, path, line_number)

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
	
	colorized_print("Finish" + str(num_of_dangerous_code), colors_list.RED)

def scan_result(is_denger, path, line):
	if (is_denger):
		colorized_print("\n  [ ! ] dangerous code found in " + path +  " at line " + str(line), colors_list.RED)
	else:
		colorized_print("\n  [ - ] dangerous code not found", colors_list.GREEN)
