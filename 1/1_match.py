import re

data = 'Sat Aug 29 04:47:00 2285::vpfhp@rjrkjelnjee.org::9961217220-5-11'
patt1 = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
patt2 = '.+?(\d+-\d+-\d+)'
m = re.match(patt1,data)
n = re.search(patt2,data)
print(m.group())
print(n.group(1))