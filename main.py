import os
import re

ServiceType = ''  #Service used for deciding connection method
ServicePort = ''  #Port the Service is running on
ServiceAddress = ''  #IP adress/Hostname used to join
Credentials = ['', '']  #Username, Password
OsCommand = ''  #Command to be compiled using user configuration
ServiceList = [
    'ssh', 'rdp', 'sql', 'sql_admin', 'vnc'
]  #Array to hold different service types from which the ServiceType variable refers to
RegexIp = re.compile(
    '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    '')


def ConfigureServiceAddress():
    LoopBool = False
    while (LoopBool == False):
        ServiceAddress = input('Please enter target ipv4 address (no ports)\n')
        if RegexIp.match(ServiceAddress):
            LoopBool = True
        else:
            print('Ipv4 Address not valid, please retry\n')
        print('Your target address is', ServiceAddress + '\n')
    return ServiceAddress


def ConfigureServicePort():
    LoopBool = False
    while (LoopBool == False):
        ServicePort = input('Please enter the port of your service\n')
        if ((65535 - (int(ServicePort))) >= 0):
            LoopBool = True
        else:
            print('Port is invalid, please retry\n')
        print('Your port is', ServicePort + '\n')
        return ServicePort


def ConfigureServiceType():
    ServiceType = ServiceList[int(
        input('Please type corrosponding menu number for you'
              'r service\n1.ssh\n2.rdp\n3.sql\n4.sql as dba\n5.vnc\n')) - 1]
    print('You have selected', ServiceType + '\n')
    return ServiceType


def ConnectService():
    os.system()
    return


def TestDisplayConfiguration():
    print('Test Message\nService Port:', ServicePort + '\nIpv4 Address:',
          ServiceAddress + '\nService Type:', ServiceType)


def SshSession():
    # Have to construct command into one variable before passing into os.system()
    os.system()
    #'plink username@host -i key.ppk' is the command to use to use putty via cmd


ServiceAddress = ConfigureServiceAddress()
ServicePort = ConfigureServicePort()
ServiceType = ConfigureServiceType()
TestDisplayConfiguration()
SshSession()

exit()
