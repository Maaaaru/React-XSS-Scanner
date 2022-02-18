
import os
from src.scan import scan_dir
from src.banner import output_banner
from src.util.printer import output_start_scanning, print_finish

rootPath = "."

def main():
	output_banner()

	output_start_scanning()

	scan_dir(rootPath)

	print_finish()

main()