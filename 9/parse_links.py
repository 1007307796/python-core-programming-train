from html.parser import HTMLParser
from io import StringIO
from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup,SoupStrainer
from html5lib import parse,treebuilders
import json

URLs = ('http://www.python.org/',)

def output(x):
    print('\n'.join(sorted(set(x))))

def simpleBS(url,f):
    output(urljoin(url,x['href']) for x in BeautifulSoup(f).find_all('a'))

def fasterBS(url,f):
#这里要报TypeError: string indices must be integers错误，暂时不知道怎么回事
    for x in BeautifulSoup(f, parse_only = SoupStrainer("a" )):
        output(urljoin(url,x['href']))

def htmlparser(url,f):
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self,'data'):
                self.data=[]
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    p = AnchorParser()
    p.feed(f.read())
    output(urljoin(url,x) for x in p.data)

def html5libparser(url,f):
    for x in parse(f):
        if isinstance(x, treebuilders.simpletree.Element) and x.name == 'a':
            output(urljoin(url,x.attributes['href']))

def process(url,data):
    print('\n*** simple BS')
    simpleBS(url,data)
    data.seek(0)
    print('\n*** faster BS')
    fasterBS(url,data)
    data.seek(0)
    print('\n***HTMLParser')
    htmlparser(url,data)
    data.seek(0)
    print('\n*** HTML5lib')
    html5libparser(url,data)

def main():
    for url in URLs:
        f = urlopen(url)
        data = StringIO(f.read().decode('utf-8'))
        f.close()
        process(url,data)

if __name__ == '__main__':
    main()