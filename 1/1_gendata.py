#!/usr/bin/env python
from random import randrange,choice
from string import ascii_lowercase as lc
from time import ctime
tlds = ('com','edu','net','org','gov')
with open('redata.txt', 'w') as f:
    f.write('')

for i in range(randrange(5,11)):
    dtint = randrange(9999999999)
    dtstr = ctime(dtint)
    llen = randrange(4,8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen,13)
    dom = ''.join(choice(lc) for j in range(dlen))
    data = "{}::{}@{}.{}::{}-{}-{}\n".format(dtstr,login,dom,choice(tlds),dtint,llen,dlen)
    with open('redata.txt','a+') as f:
        f.write(data)