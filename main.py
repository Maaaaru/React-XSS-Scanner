
import os
from src.scan import scan_dir
from src.banner import output_banner
from src.util.printer import colorized_print
from src.color import colors_list

rootPath = "."

def main():
	output_banner()

	colorized_print("[ + ] Start Scanning ...", colors_list.GREEN)

	vulnerable_files = scan_dir(rootPath)

	print_report(vulnerable_files)

def print_report(vulnerable_files):

	colorized_print("\n★★ Scan Finish!! ★★", colors_list.GREEN)

	colorized_print("\n" + "found " + str(len(vulnerable_files)) + " vulnerable file (the detailed file path is as below)", colors_list.GREEN if len(vulnerable_files) is 0 else colors_list.RED)

	print_vulnerable_files_path(vulnerable_files)


def print_vulnerable_files_path(vulnerable_files):
	for i in vulnerable_files:
		file_path = i[0]
		for l in i[1]:
			colorized_print("\n       >>> " + file_path + " at line " + str(l), colors_list.RED)

main()