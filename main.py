import os
import re
from tkinter import *
from tkinter import ttk


ServiceType = ''  # Service used for deciding connection method
ServicePort = ''  # Port the Service is running on
ServiceAddress = ''  # IP address/Hostname used to join
Credentials = ['', '']  # Username, Password
OsCommand = ''  # Command to be compiled using user configuration
ServiceList = [
    'ssh', 'rdp', 'sql', 'sql_admin', 'vnc'
]
# Array to hold different service types from which the ServiceType variable refers to
RegexIp = re.compile(
    '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    '')


def ConfigureServiceAddress():
    LoopBool = False
    while not LoopBool:
        ServiceAddress = input('Please enter target ipv4 address (no ports)\n')
        if RegexIp.match(ServiceAddress):
            LoopBool = True
        else:
            print('Ipv4 Address not valid, please retry\n')
        print('Your target address is', ServiceAddress + '\n')
    return ServiceAddress


def ConfigureServicePort():
    LoopBool = False
    while not LoopBool:
        ServicePort = input('Please enter the port of your service\n')
        if (65535 - (int(ServicePort))) >= 0:
            LoopBool = True
        else:
            print('Port is invalid, please retry\n')
        print('Your port is', ServicePort + '\n')
        return ServicePort


def ConfigureServiceType():
    ServiceType = ServiceList[int(
        input('Please type corresponding menu number for you'
              'r service\n1. SSH\n2. RDP\n3. SQL\n4. SQL as dba\n5. VNC\n')) - 1]
    print('You have selected', ServiceType + '\n')
    return ServiceType


def ConnectService():
    os.system('')
    return


def TestDisplayConfiguration():
    print('Test Message\nService Port:', ServicePort + '\nIpv4 Address:',
          ServiceAddress + '\nService Type:', ServiceType + '\n')


def ConnectRDP():
    OsCommand = ('%systemroot%/system32/mstsc.exe /v:' + ServiceAddress + ':' + ServicePort)
    print(OsCommand)


def ConnectSSH():
    OsCommand = ('plink ', Credentials[0] + '@' + ServiceAddress, ' -P ',
                 ServicePort, Credentials[1])
    OsCommand = (''.join(OsCommand))
    print('Executing the following command\n' + ''.join(OsCommand))
    os.system(''.join(OsCommand))
    # 'plink username@host -i key.ppk' is the command to use to use putty via cmd


def ClientManager():
    root = Tk()
    tree = ttk.Treeview(root)

    tree["columns"] = ("one", "two")
    tree.column("one", width=150)
    tree.column("two", width=70)
    tree.heading("one", text="Ipv4 Address")
    tree.heading("two", text="Method")

    Microsoft = tree.insert('', 0, text='Microsoft sites', values=('', ''))
    tree.insert(Microsoft, "end", text='Sub item for MC', values=('192.168.0.1', 'RDP'))
    '''
    We construct the node by :
    nodeid = tree.insert(parent, 'index', text='text to display', values=(data for first column, data for next etc))
    '''

    tree.pack()
    root.mainloop()



ClientManager()
ServiceAddress = ConfigureServiceAddress()
ServicePort = ConfigureServicePort()
ServiceType = ConfigureServiceType()

TestDisplayConfiguration()

exit()
