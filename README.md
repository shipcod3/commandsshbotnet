commandsshbotnet
================

- A command and conquer PoC mass SSH botnet
- Inspired by the mass ssh botnet in Violent Python Cookbook (my scratch for writing this ssh botnet)
- Allows you to send a command in running the script

instruction
===========
Before running commandsshbotnet.py try to test your pxssh module by running test_pxssh.py. If ever you are having this kind of error:

Traceback (most recent call last):
  File "ssh.py", line 8, in <module>
    s.login (hostname, username, password)
  File "/usr/lib/python2.7/dist-packages/pxssh.py", line 243, in login
    if not self.synch_original_prompt():
  File "/usr/lib/python2.7/dist-packages/pxssh.py", line 134, in synch_original_prompt
    self.read_nonblocking(size=10000,timeout=1) # GAS: Clear out the cache before getting the prompt
  File "/usr/lib/python2.7/dist-packages/pexpect.py", line 824, in read_nonblocking
    raise TIMEOUT ('Timeout exceeded in read_nonblocking().')

You can fix it by editing /usr/lib/python2.7/dist-packages/pxssh.py and add the following lines as indicated by the comment:

def synch_original_prompt (self):
    self.sendline()     # add this line
    time.sleep(0.5)    # add this line
    self.read_nonblocking(size=10000,timeout=1) # GAS: Clear out the cache before getting the prompt #no need to add this
    time.sleep(0.1) #no need to add this
    self.sendline() #no need to add this
    time.sleep(0.5) #no need to add this

sample usage
============
python commandsshbotnet.py "nmap localhost"

python commandsshbotnet.py "uname -a"

python commandsshbotnet.py ls

credits
=======
TJ. O'Connor (for the inspiration and the scratch of making a mass ssh botnet)
