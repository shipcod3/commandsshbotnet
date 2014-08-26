# commandsshbotnet.py
# author: @shipcod3
# 
# >> used for testing the pxssh module

import pxssh
import getpass
try:
    s = pxssh.pxssh()
    hostname = raw_input('SET HOST: ')
    username = raw_input('SET USERNAME: ')
    password = getpass.getpass('SET PASSWORD: ')
    s.login (hostname, username, password)
    s.sendline ('uname -a')   # run a command
    s.prompt()             # match the prompt
    print s.before          # print everything before the prompt.
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)
