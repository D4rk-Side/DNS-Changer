import subprocess, re, os, time

dns_dict = {
    'Cloudflare' : ['1.1.1.1', '1.0.0.1'],
    'Google public' : ['8.8.8.8', '8.8.4.4'],
    'OpenDNS' : ['208.67.222.222', '208.67.220.220'],
    'Shecan' : ['178.22.122.100', '185.51.200.2'],
    'Azad(403)' : ['10.202.10.202', '10.202.10.102'],
    'Begzar' : ['185.55.226.26', '185.55.225.25'],
    'Electro' : ['78.157.42.100', '78.157.42.101'],
    'Quad9' : ['9.9.9.9', '149.112.112.112'],
    'CleanBrowsing' : ['185.228.168.9', '185.228.169.9'],
    'Comodo Secure' : ['8.26.56.26', '8.20.247.20'],
    'Alternate': ['76.76.19.19', '76.223.122.150'],
    'OpenNIC': ['216.87.84.211', '23.90.4.6'],
    'Verisign public': ['64.6.64.6', '64.6.65.6'],
    'Level3': ['209.244.0.3', '209.244.0.4'],
    'DYN': ['216.146.35.35', '216.146.36.36'],
    'Safe': ['195.46.39.39', '195.46.39.40'],
    'DNS.Watch': ['84.200.69.80', '84.200.70.40'],
    'Shelter public': ['94.103.125.157', '94.103.125.158'],
    'Beshkan': ['181.41.194.177', '181.41.194.186'],
    'Radar': ['10.202.10.10', '10.202.10.11'],
    'Pishgaman': ['5.202.100.100', '5.202.100.101'],
    'NextDNS': ['45.90.28.0', '45.90.30.0'],
    'ControlD': ['76.76.2.0', '76.76.10.0'],
    'AdGuard (Family)': ['176.103.130.130', '176.103.130.131'],
    'AdGuard (Gaming)': ['94.140.14.14', '94.140.15.15'],
    'SmartViper': ['208.76.50.50', '208.76.51.51'],
    'CenturyLink': ['205.171.3.65', '205.171.2.65'],
    'Neustar': ['156.154.70.22', '156.154.71.22'],
    'FreeDNS': ['37.235.1.174', '37.235.1.177'],
    'Yandex (Basic)': ['77.88.8.8', '77.88.8.1'],
    'Yandex (Safe)': ['77.88.8.88', '77.88.8.2'],
    'Yandex (Family)': ['77.88.8.7', '77.88.8.3']
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
    dc = (int(abs(float(len(str(dl)) - 17) // 2)) * ' ' + f'({dl})' + int(abs(float(len(str(dl)) - 19) / 2)) * ' ')
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
    net_names = []
    net_types = []
    net_devices = []
    connections = str(subprocess.run(['nmcli', 'con', 'show'], capture_output=True).stdout).strip("b'").split('\\n')
    for connection in range(1, len(connections) - 1):
        net_names.append(str(connections[connection].split('  ')[0]))
        net_types.append(str(connections[connection]).rstrip(' ').split('  ')[-2])
        net_devices.append(str(connections[connection]).rstrip(' ').split('  ')[-1])
    nl_head = ('    ' + 105 * '_')
    nl_body = ('    |' + 103 * '-' + '|')
    print(nl_head, '    |' + (18 * ' ') + 'Network name' + (
                18 * ' ') + '| Connection type |' + ' Connection device |' + ' Network number |', nl_body, sep='\n')
    for i in range(len(net_names)):
        nn = (int(abs(float(len(net_names[i]) - 48) // 2)) * ' ' + f'{net_names[i]}' + int(
            abs(float(len(net_names[i]) - 48) / 2)) * ' ')  # 'nn' -> Network name
        nt = (int(abs(float(len(net_types[i]) - 17) // 2)) * ' ' + f'{net_types[i]}' + int(
            abs(float(len(net_types[i]) - 17) / 2)) * ' ')
        nd = (int(abs(float(len(net_devices[i]) - 19) // 2)) * ' ' + f'{net_devices[i]}' + int(
            abs(float(len(net_devices[i]) - 19) / 2)) * ' ')
        nc = (int(abs(float(len(str(i)) - 14) // 2)) * ' ' + f'({i + 1})' + int(abs(float(len(str(i)) - 14) / 2)) * ' ')
        print('    |' + nn + '|' + nt + '|' + nd + '|' + nc + '|', nl_body, sep='\n')
    ns = int(input('\nselect your network: '))
    slicer = net_names[ns - 1]
    slicer = slicer.replace(' ', r'\ ')


    def dns_loader_linux(dnscode):
        os.system(f'nmcli con mod {slicer} ipv4.dns {dns_dict[dnscode][0]}')
        os.system(f'nmcli con mod {slicer} +ipv4.dns {dns_dict[dnscode][1]}')
        os.system(f'nmcli con mod {slicer} ipv4.ignore-auto-dns yes')
        os.system(f'nmcli con down {slicer} && nmcli con up {slicer}')


    if sd == 'd':
        os.system(f'nmcli con mod {slicer} ipv4.ignore-auto-dns no')
        print(f"Your DNS has been restored to its original state.\nGood luck!")
        time.sleep(2)
        os.system('clear')
    else:
        dns_loader_linux((dls[int(sd) - 1]))
        print(f"You are now using the '{(dls[int(sd) - 1])}' DNS \nGood luck!")
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
            print('    |     Ethernet    |' + nn + '|' + nc + '|', body, sep='\n')
            nl.append(network)

        for network in cwnf:
            num += 1
            nn = (int(abs(float(len(network) - 48) // 2)) * ' ' + f'{network}' + int(abs(float(len(network) - 48) / 2)) * ' ' )  # 'nn' -> Network name
            nc = (f'        ({num})         ')  # 'nc' -> Network code
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
    elif sd != 'f' and sd != 'd':
        dns_loader_windows((dls[int(sd) - 1]), dls[int(sd) - 1])
    else:
        print('Something went wrong!')
