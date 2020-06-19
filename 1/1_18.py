import re

dicWeek = {'Mon':'0','Tue':'0','Wed':'0','Thu':'0','Fri':'0','Sat':'0','Sun':'0'}
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
f = open('redata.txt','r')
for line in f.readlines():
    m = re.match(patt,line)
    if m is not None:
        temp = m.group()
        dicWeek[temp]=str(int(dicWeek[temp])+1)
f.close()
print(str(dicWeek))