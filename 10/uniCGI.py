#!/usr/bin/env python

CODEC = 'gbk'
UNICODE_HELLO = '''
Hello!
Hola!
\u4F60\u597D!
\u3053\u3093\u306B\u3061\u306F!
'''

print('''Content-Type: text/html; charset=%s

<HTML><HEAD><TITLE>Unicode CGI Demo</TITLE></HEAD>
<BODY><H1>Unicode CGI Demo</H1><P>
<BIG>%s</BIG></BODY></HTML>
'''  % (CODEC, UNICODE_HELLO))
