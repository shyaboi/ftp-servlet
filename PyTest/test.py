from ftplib import FTP
import os
from dotenv import load_dotenv

load_dotenv()
PASS = os.getenv('PASS')

ftp = FTP('server308.com')
try:
    ftp.login('joinsoca', PASS)
    dirName = './www/rebuild'
    files = ftp.nlst()
    print(files)
except:
  print('oh dear.')
  ftp.quit()

try:
    for fileName in files:
        if "."  in fileName:
            print('Downloading....')
            ftp.retrbinary('RETR ' + fileName, open(fileName, 'wb').write)
        elif "." not in fileName :
            print('some dir i guess...or done...idk')
except:    
    print('oh dear.')
    ftp.quit()
# import ftplib

# with ftplib.FTP('server308.com') as ftp:
    
#     try:
#         ftp.login('joinsoca', 'vF<^aPt]!%B{+!779b#h') 

#         files = []

#         ftp.dir(files.append)

#         print(files)
            
#     except ftplib.all_errors as e:
#         print('FTP error:', e)