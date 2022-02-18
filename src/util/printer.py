class colors_list:
	CYAN = '\033[36m'
	GREEN = '\033[32m'
	MAGENTA = '\033[35m'

def colorized_print(text,color_code):
	end = '\033[0m'

	print(color_code + text + end)