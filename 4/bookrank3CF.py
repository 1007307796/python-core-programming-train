#coding:gbk
from atexit import register
from concurrent.futures import ThreadPoolExecutor
from re import compile
from threading import Thread
from time import ctime
import urllib.request
import re

COOKIE = 'session-id=147-6202719-8323527; session-id-time=2082787201l; ' \
         'i18n-prefs=USD; sp-cdn="L5Z9:CN"; ubid-main=135-5892049-9419614; ' \
         'x-wl-uid=1x+wqCxMzpByN//cOJ2RVSJH6AIK8vCk8Cl1O77NwlMB5862DmhRZXDMG6O24WwekJ741RvZd8LQ=; ' \
         'session-token="l3M1fteQzUgDqtkPYtbYhCL+TPPrKOYigrULYkdI5bKy/' \
         'Gua9JGYnsLlKa+TW1ZqBPWPZdXllaL2wJkObEp+i+LbIYf5TKXfwIcqLkcQeuR17OdF/' \
         'NaxVgKr6V5sFV354S71mjSJlSODhEDYCzKoUXC8fBVWTZ4N+Bagnkf+nUTAvSIcnyWnQX8LS' \
         'mQzeAazS5hQ9lUKhBmKyyO0NJw4MEzx+QeVEjFRBta7T8LeIYyyz4QhjX+9wvK98TYoD5w0bQeEtPK6oWs="; ' \
         'csm-hit=tb:VRE0G7QCC6K14D8533S8+b-BGAPT8DVW7ZZ7PSRMXXZ|1592966702105&t:1592966702105&adb:adblk_no'
UT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Chrome/83.0.4103.106 Safari/537.36'
HEADERs = {
    'cookie':COOKIE,
    'user-agent':UT,
}
REGEX = compile(b'#([\d,]+) in Books ')
AMZN = 'https://www.amazon.com/dp/'
ISBNs = {
    '0132269937':'Core Python Programming',
    '0132356139':'Python Web Development with Django',
    '0137143419':'Python Fundamentals LiveLessons',
}

def getRanking(isbn):
    resp = urllib.request.Request('{}{}'.format(AMZN,isbn),headers=HEADERs)
    page = urllib.request.urlopen(resp)
    data = page.read()
    page.close()
    return str(REGEX.findall(data)[0],'utf-8')

def _main():
    print('At',ctime(),'on Amazon...')
    with ThreadPoolExecutor(3) as executor:
        #map()如果传入一个字典，则返回key构成的列表
        for isbn,ranking in zip(ISBNs,executor.map(getRanking,ISBNs)):
            print('- {} ranked {}'.format(ISBNs[isbn], ranking))
    print('all done at:', ctime())

if __name__ == '__main__':
    _main()