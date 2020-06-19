import os
import re

with os.popen('tasklist /nh','r') as f:
	for el in f:
		print(re.findall(r'([\w.+]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',el.strip())) 