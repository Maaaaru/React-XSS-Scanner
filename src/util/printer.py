from src.color import colors_list

def colorized_print(text,color_code):
	end = '\033[0m'

	print(color_code + text + end)


def print_start():
	colorized_print("[ :: ] Start Scanning ... \n", colors_list.GREEN)

def print_finish():
	colorized_print("\n Scan Finish!!", colors_list.GREEN)