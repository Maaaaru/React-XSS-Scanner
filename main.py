
import os
import src.scan as s
from src.banner import output_banner,output_start_scanning

rootPath = "."

def main():
	output_banner()

	output_start_scanning()

	s.scan_dir(rootPath)

main()