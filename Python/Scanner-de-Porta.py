import socket
import os
os.system("clear")
print('''
******************************************************
******************************************************
***    ____            _   ____                    ***
***   |  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __    ***
***   | |_) / _ \| '__| __\___ \ / __/ _` | '_ \   ***
***   |  __/ (_) | |  | |_ ___) | (_| (_| | | | |  ***
***   |_|   \___/|_|   \__|____/ \___\__,_|_| |_|  ***
***                                 Paulo Rafael   ***
******************************************************
******************************************************
''')
print()
ip = input("Digite o ip:")
portas  = {
21:"TCP FTP",
22:"TCP SSH",
23:"TCP Telnet",
25:"TCP SMTP",
53:"UDP DNS",
69:"UDP TFTP",
80:"TCP HTTP",
110:"TCP POP3",
123:"UDP NTP",
143:"TCP IMAP",
177:"TCP XDMCP",
389:"TCP LDAP",
443:"TCP HTTPS",
445:"TCP CIFS"}
for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    codigo = cliente.connect_ex((ip,porta))
    if codigo == 0:
        print (porta,portas[porta],"Aberta")
    else:
        print (porta,portas[porta],"Fechada")


