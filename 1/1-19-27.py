import re

patt19 = '[\w]{3}\s[\w]{3}\s\s?[\d]+\s[\d]+:[\d]+:[\d]+'
patt26 = '(\w+@\w+\.\w{3})'
patt27 = '\w{3}\s(\w{3})\s\s?(\d{1,2})\s[^\s]+\s(\d{4}).+'
f = open('redata.txt','r')
for line in f.readlines():
    print(re.sub(patt27,r'\1,\2,\3',line))
    print(re.match(patt19,line.rstrip()).group())
    print(re.sub(patt26, '1111111111@qq.com', line))
f.close()