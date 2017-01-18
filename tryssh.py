import os
import sys
import os.path
from pexpect import pxssh



try:
    txt = sys.argv[1]
except IndexError:
    print "Use python testip xxx.txt(server list txt file)"
    os._exit(0)
	
	
if os.path.exists(txt):
    d = open(txt)
    lines = d.readlines()
    if len(lines) != 0:
        linesnum = len(lines)
        print linesnum,"Server Found"
    else:
        print "The file is empty"
else:
    print 'file does not exist '

def tryssh(ip,user,password):
    try:
        s = pxssh.pxssh()
        s.prompt(timeout=10)
        if not s.login (ip,user,password):
            return ip," SSH session failed on login."
            #print str(s)
        else:
            return ip," SSH session login successful"
            #s.sendline ('ls -l')
            #s.prompt()         # match the prompt
            #print s.before     # print everything before the prompt.
            s.logout()
    except:
        return ip," SSH session failed on login."
    


d = open(txt)
line = d.readline()
while line:
    line = line.strip()
    server = line.split(" ")
    print tryssh(server[0],server[1],server[2])
    line = d.readline()
d.close()
        
    




