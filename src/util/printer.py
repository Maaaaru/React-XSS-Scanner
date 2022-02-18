def colorized_print(text,color_code):
	end = '\033[0m'

	print(color_code + text + end)