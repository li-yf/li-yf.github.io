
favor_file = ''
import os, re
for i in os.listdir("D:\\"):
	if re.match("Microsoft_Edge_‎.*.html", i):
		favor_file = i
		break
if favor_file == '':
	print("favor file not found!")

head_cnt = 7
import os
with open(os.sep.join(["D:", favor_file]), 'r', encoding='UTF-8') as f1:
	with open("English-Listening-1010.html", 'w', encoding='UTF-8') as f2:

		found = False
		for line in f1:
			## first head_cnt lines copy from f1 to f2
			if head_cnt > 0:
				head_cnt -= 1
				f2.write(line)
				continue
			
			if not found:
				if re.search("English Listening", line):
					found = True
			else:
				f2.write(line)
				if re.search("/DL", line):					
					break
