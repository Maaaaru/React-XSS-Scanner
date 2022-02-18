import time
from src.util.printer import colorized_print
from src.color import colors_list

interbal = 1 / 16
author = "Maaaaru"
github = "https://github.com/Maaaaru/React-XSS-Scanner"
version = "v1.0.0"

separation = ">>-----------------------------------------------------------------------------------------------"

b1 = "██████╗ ███████╗ █████╗  ██████╗████████╗  ██╗  ██╗███████╗███████╗      ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗"
b2 = "██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝  ╚██╗██╔╝██╔════╝██╔════╝      ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗"
b3 = "██████╔╝█████╗  ███████║██║        ██║█████╗╚███╔╝ ███████╗███████╗█████╗███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝"
b4 = "██╔══██╗██╔══╝  ██╔══██║██║        ██║╚════╝██╔██╗ ╚════██║╚════██║╚════╝╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗"
b5 = "██║  ██║███████╗██║  ██║╚██████╗   ██║     ██╔╝ ██╗███████║███████║      ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║"
b6 = "╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  " + version + "\n"
b7 = separation
b8 = "\n        Author -- " + author
b9 = "\n        Github -- " + github + "\n"
b10 = separation + "\n"

def output_banner():	
	for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]:
		colorized_print(b,colors_list.CYAN)

		time.sleep(interbal)