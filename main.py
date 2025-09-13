import subprocess, re, os, time

cf_t = ('Cloudflare', '1.1.1.1', '1.0.0.1')
g_t = ('Google public', '8.8.8.8', '8.8.4.4')
od_t = ('OpenDNS', '208.67.222.222', '208.67.220.220')
sh_t = ('Shecan', '185.51.200.2', '178.22.122.100')
a_t = ('Azad(403)', '10.202.10.202', '10.202.10.102')
b_t = ('Begzar', '185.55.226.26', '185.55.225.25')
e_t = ('electro', '78.157.42.100', '78.157.42.101')
dns_dict = {
    'Cloudflare' : ['1.1.1.1', '1.0.0.1'],
    'Google public' : ['8.8.8.8', '8.8.4.4'],
    'OpenDNS' : ['208.67.222.222', '208.67.220.220'],
    'Shecan' : ['185.51.200.2', '178.22.122.100'],
    'Azad(403)' : ['10.202.10.202', '10.202.10.102'],
    'Begzar' : ['185.55.226.26', '185.55.225.25'],
    'electro' : ['78.157.42.100', '78.157.42.101']
}
print('Welcome to DNS changer')
dl = 0
dl_head = ('     ' + 42 * '_')  # 'dl_head' -> Dns list header
dl_body = ('     |' + 40 * '-' + '|')  # 'dl_body' -> Dns list body
dl_foot = ('     |>>>>>>>>> created by D4rk $ide <<<<<<<<<|' + '\n' +'     ' + 42 * '-')  # 'dl_foot' -> Dns list footer
print(dl_head, '     |  DNS server name  |  DNS server number |', dl_body, sep='\n')
dls = []
for dns in dns_dict:
    dl += 1
    dn = (int(abs(float(len(dns) - 19) // 2)) * ' ' + f'{dns}' + int(abs(float(len(dns) - 19) / 2)) * ' ')
    dc = (f'        ({dl})         ')
    print('     |' + dn + '|' + dc + '|', dl_body, sep='\n')
    dls.append(dns)
DHCP = (int(abs(float(len('DHCP') - 19) // 2)) * ' ' + 'DHCP' + int(abs(float(len('DHCP') - 19) / 2)) * ' ')
Flush = (int(abs(float(len('flush DNS') - 19) // 2)) * ' ' + 'flush DNS' + int(abs(float(len('flush DNS') - 19) / 2)) * ' ')
print('     |' + DHCP + '|        (d)         |', dl_body, '     |' + Flush + '|        (f)         |', dl_body, dl_foot, sep='\n')
sd = input('select dns: ')  # 'sd' -> selected DNS
if sd == 'f':
    uo = input("""    ___________________________
    | OS name |   OS number   |
    |-------------------------|
    |  Linux  |      (-)      |
    |-------------------------|
    | Windows |      (2)      |
    |-------------------------|
    |   Mac   |      (-)      |
    |-------------------------|

select your os: """)  # 'uo' -> user os
else:
    uo = input("""    ___________________________
    | OS name |   OS number   |
    |-------------------------|
    |  Linux  |      (1)      |
    |-------------------------|
    | Windows |      (2)      |
    |-------------------------|
    |   Mac   | Coming soon...|
    |-------------------------|

select your os: """)
if uo == '1':  # Linux section
    if sd == '1':
        os.system(f'echo nameserver {cf_t[1]} > /etc/resolv.conf && echo nameserver {cf_t[2]} >> /etc/resolv.conf')
    elif sd == '2':
        os.system(f'echo nameserver {g_t[1]} > /etc/resolv.conf && echo nameserver {g_t[2]} >> /etc/resolv.conf')
    elif sd == '3':
        os.system(f'echo nameserver {od_t[1]} > /etc/resolv.conf && echo nameserver {od_t[2]} >> /etc/resolv.conf')
    elif sd == '4':
        os.system(f'echo nameserver {sh_t[1]} > /etc/resolv.conf && echo nameserver {sh_t[2]} >> /etc/resolv.conf')
    elif sd == '5':
        os.system(f'echo nameserver {a_t[1]} > /etc/resolv.conf && echo nameserver {a_t[2]} >> /etc/resolv.conf')
    elif sd == '6':
        os.system(f'echo nameserver {b_t[1]} > /etc/resolv.conf && echo nameserver {b_t[2]} >> /etc/resolv.conf')
    else:
        print('please type your dns server code.')
    udl = subprocess.run(['cat', '/etc/resolv.conf'], capture_output=True).stdout.decode()  # 'udl' -> user dns linux
    udlf = tuple(re.findall('nameserver (.*)', udl))  # 'udlf' -> user dns linux find
    if udlf == cf_t[1:]:
        print(f"You are now using the '{cf_t[0]}' DNS \nGood luck!")
        time.sleep(2)
        os.system('clear')
    elif udlf == g_t[1:]:
        print(f"You are now using the '{g_t[0]}' DNS \nGood luck!")
        time.sleep(2)
        os.system('clear')
    elif udlf == od_t[1:]:
        print(f"You are now using the '{od_t[0]}' DNS \nGood luck!")
        time.sleep(2)
        os.system('clear')
    elif udlf == sh_t[1:]:
        print(f"You are now using the '{sh_t[0]}' DNS \nGood luck!")
        time.sleep(2)
        os.system('clear')
    elif udlf == a_t[1:]:
        print(f"You are now using the '{a_t[0]}' DNS \nGood luck!")
        time.sleep(2)
        os.system('clear')
    elif udlf == b_t[1:]:
        print(f"You are now using the '{b_t[0]}' DNS \nGood luck!")
        time.sleep(2)
        os.system('clear')

elif uo == '2':  # Windows section
    cnc = subprocess.run(['ipconfig', '/all'], capture_output=True).stdout.decode()  # 'cnc' -> cmd network check
    cenf = list(re.findall('Ethernet adapter (.*):', cnc))  # 'cenf' -> cmd ethernet network find
    cwnf = list(re.findall('Wireless LAN adapter (.*):', cnc))  # 'cwnf' -> cmd wifi network find
    if sd == 'f':
        cfd = subprocess.run(['ipconfig', '/flushdns'])  # 'cfd' -> Cmd flush DNS
        time.sleep(2)
        os.system('cls')
    else:
        num = 0
        nl = []  # 'nl' -> Network list
        head = ('    ' + 89 * '_')
        body = ('    |' + 87 * '-' + '|')
        print(head, '    | Connection type |' + (18 * ' ') + 'Network name' + (18 * ' ') + '|   Network number   |', body, sep='\n')
        for network in cenf:
            num += 1
            nn = (int(abs(float(len(network) - 48) // 2)) * ' ' + f'{network}' + int(abs(float(len(network) - 48) / 2)) * ' ' )  # 'nn' -> Network name
            nc = (f'        ({num})         ')  # 'nc' -> Network code
            # print('    |' + int(abs(float(len(network) - 48) // 2)) * ' ' + f'{network}' + int(abs(float(len(network) - 48) / 2)) * ' ' + '|' + f'        ({num})         |', body, sep='\n')
            print('    |     Ethernet    |' + nn + '|' + nc + '|', body, sep='\n')
            nl.append(network)

        for network in cwnf:
            num += 1
            nn = (int(abs(float(len(network) - 48) // 2)) * ' ' + f'{network}' + int(abs(float(len(network) - 48) / 2)) * ' ' )  # 'nn' -> Network name
            nc = (f'        ({num})         ')  # 'nc' -> Network code
            # print('    |' + int(abs(float(len(network) - 48) // 2)) * ' ' + f'{network}' + int(abs(float(len(network) - 48) / 2)) * ' ' + '|' + f'        ({num})         |', body, sep='\n')
            print('    |      Wi-Fi      |' + nn + '|' + nc + '|', body, sep='\n')
            nl.append(network)
        ns = int(input('\nselect your network: '))  # 'ns' -> Network select
    def dns_loader_windows(dnscode, dnsname):
        subprocess.run(['netsh', 'interface', 'ip', 'set', 'dns', f'name="{nl[ns-1]}"', 'static', dns_dict[dnscode][0]])
        subprocess.run(['netsh', 'interface', 'ip', 'add', 'dns', f'name="{nl[ns-1]}"', dns_dict[dnscode][1], 'index=2'])
        print(f"You are now using the '{dnsname}' DNS \nGood luck!")
        time.sleep(2)
        os.system('cls')
    if sd == 'd':
        cpds = subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dnsservers', f'name="{nl[ns-1]}"', 'source=dhcp'])
        print(f"Now your DNS set on Dynamic Host Configuration Protocol(DHCP) \nGood luck!")
        time.sleep(2)
        os.system('cls')
    elif sd == 'f':
        pass
    elif sd != None:
        dns_loader_windows((dls[int(sd) - 1]), dls[int(sd) - 1])
    else:
        print('Something went wrong!')