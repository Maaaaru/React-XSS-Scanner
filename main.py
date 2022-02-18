
import os
from src.scan import scan_dir
from src.banner import output_banner
from src.util.printer import print_start, print_finish

rootPath = "."

def main():
	output_banner()

	print_start()

	scan_dir(rootPath)

	print_finish()

main()