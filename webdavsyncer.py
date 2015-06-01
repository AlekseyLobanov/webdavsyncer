#!/usr/bin/python3

import sys
import webdav.client as wc

def main(argv):
    if len(argv) != 3 or (argv[0] in ['h','-h','H']):
        print("""Usage:
webdavsyncer.py SETTINGS_FILE LOCAL_PATH REMOTE_NAME
For example: webdavsyncer.py ~/settings.txt ~/cats_23.jpg cat3.jpg
And settings.txt is:
{
    'webdav_hostname': "https://webdav.URL.com",
    'webdav_login': "LOGIN",
    'webdav_password': "PASSWORD",
    'rem_path': "Backups/"
}""")
        return

    opts = eval(open(argv[0]).read())
    client = wc.Client(opts)
    client.upload_sync(
        remote_path=opts['rem_path']+argv[2], 
        local_path=argv[1]
    )
    

if __name__ == '__main__':
    main(sys.argv[1:])
