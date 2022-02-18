
import os
from src.scan import scan_dir
from src.banner import output_banner
from src.util.printer import colorized_print
from src.color import colors_list

rootPath = "."

def main():
	output_banner()

	print_start_scan()

	vulnerable_files = scan_dir(rootPath)

	print_scan_result(vulnerable_files)

def print_start_scan():
	colorized_print("[ + ] Start Scanning ...", colors_list.GREEN)

def print_scan_result(vulnerable_files):
	colorized_print("\n═════════════════════════════════════════════════════════════════ <<", colors_list.WHITE)

	colorized_print("\n   ★★ Scan Finish!! ★★", colors_list.GREEN)

	colorized_print("\n   " + str(len(vulnerable_files)) + " vulnerable file found (the detailed file path is as below)", colors_list.GREEN if len(vulnerable_files) is 0 else colors_list.RED)

	print_vulnerable_files_path(vulnerable_files)

	colorized_print("\n═════════════════════════════════════════════════════════════════ <<", colors_list.WHITE)

def print_vulnerable_files_path(vulnerable_files):
	for i in vulnerable_files:
		colorized_print("\n       >>> " + i[0] + " at line " + str(i[1]), colors_list.RED)

main()