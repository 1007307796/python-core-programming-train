import ftplib
import os
import socket

HOST = 'www.3gpp.org'
DIRN = 'PCG/PCG_01/Docs'
FILE = 'PCG1_09.pdf'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print('ERROR:cannot reach ',HOST)
        return
    print('*** Connected to host ',HOST)
    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR:cannot login anonymously')
        f.quit()
        return
    print('*** Logged in as "anonymously"')
    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR:cannot CD to ',DIRN)
        f.quit()
        return
    print('*** Changed to {} folder'.format(DIRN))
    try:
        f.retrbinary('RETR {}'.format(FILE),open(FILE,'wb').write)
    except ftplib.error_perm:
        print('ERROR:cannot read file ',FILE)
        os.unlink(FILE)
    else:
        print('*** Downloaded {} to CWD'.format(FILE))
    f.quit()
if __name__ == '__main__':
    main()