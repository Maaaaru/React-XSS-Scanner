import argparse
import os
from src.scan import scan_dir
from src.banner import output_banner
from src.util.printer import colorized_print
from src.color import colors_list

default_scan_path = ".."

def main(scan_path):
	output_banner()

	colorized_print("[ + ] Start Scanning ...", colors_list.GREEN)

	try:
		vulnerable_files = scan_dir(scan_path)

		print_report(vulnerable_files)
	except:
		colorized_print("\nAn unknown error has occurred...  Please try again later", colors_list.RED)

def print_report(vulnerable_files):

	colorized_print("\n--------------------------------------------------------------------", colors_list.WHITE)
	colorized_print("\n★★ Scan Finish!! ★★", colors_list.GREEN)

	if len(vulnerable_files) > 0:
		colorized_print("\n" + "found " + str(len(vulnerable_files)) + " vulnerable file (the detailed file path is as below)", colors_list.GREEN if len(vulnerable_files) == 0 else colors_list.RED)
	else:
		colorized_print("\nvulnerable file not found\n", colors_list.GREEN)
		
	print_vulnerable_files_path(vulnerable_files)


def print_vulnerable_files_path(vulnerable_files):
	for i in vulnerable_files:
		file_path = i[0]
		for l in i[1]:
			colorized_print("\n  >>> " + file_path + " at line " + str(l), colors_list.RED)


if __name__ == '__main__':
	parser = argparse.ArgumentParser("React XSS Scanner")

	parser.add_argument('--path', '-P', help='Directly path to scan')

	args = parser.parse_args()

	main(args.path if args.path else default_scan_path)