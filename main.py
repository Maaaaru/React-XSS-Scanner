
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

	colorized_print("\nScan Finish!!", colors_list.GREEN)

	colorized_print("\n" + str(len(vulnerable_files)) + " vulnerable file found", colors_list.GREEN if len(vulnerable_files) is 0 else colors_list.RED)

main()