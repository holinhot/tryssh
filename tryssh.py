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
    s = pxssh.pxssh()
    if not s.login (ip,user,password):
        print "SSH session failed on login."
        #print str(s)
    

    else:
        print "SSH session login successful"
        #s.sendline ('ls -l')
        #s.prompt()         # match the prompt
        #print s.before     # print everything before the prompt.
        s.logout()
        
    




