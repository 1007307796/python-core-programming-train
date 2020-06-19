#!/usr/bin/env python
#encoding: utf-8
import re

patt1 = '[bh][aiu]t'
patt2 = '[A-Za-z-]+ [A-Za-z-]+'
patt3 = '[A-Za-z-]+, [A-Za-z]'
patt4 = '^[a-zA-Z_]\w+'
patt5 = r'([\u4e00-\u9fa5]{2,7}?(?:省|市|自治区)){0,2}([\u4e00-\u9fa5]{2,7}?(?:市|区|县)){0,2}' \
        r'([\u4e00-\u9fa5]{2,7}?(?:镇|县|村)){1,2}'
patt6 = '^www[\.:/a-zA-Z]+.com$'
patt7 = '\d+'
patt8 = '\d+[lL]'
patt9 = '\d+\.(\d+)?'
patt10 = '[\d\.e-]+[+-][\d]+[Jj]'
patt11 = '[\w]+(\.[\w]+)*@[\w]+(\.[\w]+)+'
patt12 = '[a-zA-z]+://[^\s]*'
patt13 = "<type '([\w_]+)'>"
patt14 = '1[012]'
patt15 = '([\d]{4}-[\d]{4}-[\d]{4}-[\d]{4})|([\d]{4}-[\d]{6}-[\d]{5})'
patt28 = '(\d{3}-)?\d{3}-\d{4}'
patt29 = '(\d{3}-)?(\(\d{3}\))?\d{3}-\d{4}'
print(re.match(patt1,'bat').group())
print(re.match(patt2,'Jack Wilion').group())
print(re.match(patt3,'Jack, Wilion').group())
print(re.match(patt4,'flag').group())
print(re.match(patt5,'四川省成都市郫都区红光镇').group())
print(re.match(patt6,'www.baidu.com').group())
print(re.match(patt7,'12345').group())
print(re.match(patt8,'100000L').group())
print(re.match(patt9,'75.').group())
print(re.match(patt10,'12.3+4j').group())
print(re.match(patt11,'1111111111@qq.com').group())
print(re.match(patt12,'https://tool.oschina.net/regex/#').group())
print(re.match(patt13,"<type 'float'>").group(1))
print(re.match(patt14,"10").group())
print(re.match(patt15,"2031-2134-9008-0000").group())
print(re.match(patt28,"555-1212").group())
print(re.match(patt29,"(800)555-1212").group())