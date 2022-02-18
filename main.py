
import os
import src.scan_dir as s
import src.banner as b

rootPath = "."

def main():
	b.output_banner()

	s.scan_dir(rootPath)

main()