import nntplib
import socket

HOST = 'web.aioe.org'
GENM = 'comp.lang.pythons'
USER = ''
PASS = ''

def main():
    try:
        n = nntplib.NNTP(HOST)
        #,user=USER,password=PASS)
    except socket.gaierror as e:
        print('ERROR:cannot reach host:',HOST)
        print('    ',eval(str(e))[1])
        return
    except nntplib.NNTPPermanentError as e:
        print('ERROR:access denied on ',HOST)
        print('    ',str(e))
        return
    print('***Connected to host ',HOST)
    try:
        rsp,ct,fst,lst,grp = n.group(GENM)
    except nntplib.NNTPPermanentError as ee:
        print('ERROR:cannot load group ',GENM)
        print('    ',str(ee))
        print('    Server may require authentication')
        print('    Uncomment/edit login line above')
        n.quit()
        return
    except nntplib.NNTPPermanentError as ee:
        print('ERROR:group {} unavailable'.format(GENM))
        print('    ',str(ee))
        n.quit()
        return
    print('*** Found newsgroup ',GENM)
    rng = '{}-{}'.format(lst,lst)
    rsp,frm = n.xhdr('from',rng)
    rsp,sub = n.xhdr('subject',rng)
    rsp,dat = n.xhdr('date',rng)
    print('''***Found last article (#{}):
    
    From:{}
    Subject:{}
    Date:{}
    '''.format(lst,frm[0][1],sub[0][1],dat[0][1]))
    rsp,data = n.body(lst)
    displayFirst20(data)
    n.quit()

def displayFirst20(data):
    print('*** First (<=20) meaningful lines:\n')
    count = 0
    lines = (line.rstrip() for line in data[2])
    lastBlank = True
    for line in lines:
        if line:
            lower = line.lower()
            if (lower.startswith(b'>') and not lower.startswith(b'>>>')) or \
                lower.startswith(b'|') or \
                lower.startswith(b'in article') or \
                lower.endswith(b'writes:') or \
                lower.endswith(b'wrote:'):
                    continue
            if not lastBlank or (lastBlank and line):
                print('    ',line.decode('utf-8'))
                if line:
                    count +=1
                    lastBlank = False
                else:
                    lastBlank = True
            if count == 20:
                break
if __name__ == '__main__':
    main()
