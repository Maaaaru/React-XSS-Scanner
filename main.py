
import os
from src.scan import scan_dir
from src.banner import output_banner
from src.util.printer import colorized_print
from src.color import colors_list

rootPath = ".."

def main():
	output_banner()

	colorized_print("[ + ] Start Scanning ...", colors_list.GREEN)

	scan_dir(rootPath)

	colorized_print("\n Scan Finish!!", colors_list.GREEN)

main()