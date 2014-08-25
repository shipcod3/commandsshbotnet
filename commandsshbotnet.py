# commandsshbotnet.py
# author: @shipcod3
# inspired by the mass ssh botnet in " Violent Python Cookbook "

import optparse
import pxssh
import sys

print "[*-*] Engine start.........."

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
    print "Sample Usage: python commandsshbotnet.py <command>"

def main(argv):
    if len(argv) < 2:
        return usage()

    os_command = sys.argv[1]

    def botnetCommand(command):
        for client in botNet:
            output = client.send_command(command)
            print '[*] IP: ' + client.host
            print '[+] Command: ' + output

    def addConfig(host, user, password):
        client = Client(host, user, password)
        botNet.append(client)

    botNet = []
    #add your host, user, and password here 
    addConfig('127.0.0.1', 'celso', 'celso123') #sample config
    addConfig('127.0.0.2', 'celso', 'celso123')
    botnetCommand(os_command)

if __name__ == "__main__":
    main(sys.argv)
