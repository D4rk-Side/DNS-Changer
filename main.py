import subprocess, re, os, time, platform

dns_dict = {
    'AdGuard (Family)': ['176.103.130.130', '176.103.130.131'],
    'AdGuard (Gaming)': ['94.140.14.14', '94.140.15.15'],
    'Alternate': ['76.76.19.19', '76.223.122.150'],
    'Azad(403)' : ['10.202.10.202', '10.202.10.102'],
    'Begzar' : ['185.55.226.26', '185.55.225.25'],
    'Beshkan': ['181.41.194.177', '181.41.194.186'],
    'CenturyLink': ['205.171.3.65', '205.171.2.65'],
    'CleanBrowsing' : ['185.228.168.9', '185.228.169.9'],
    'Cloudflare' : ['1.1.1.1', '1.0.0.1'],
    'Comodo Secure' : ['8.26.56.26', '8.20.247.20'],
    'ControlD': ['76.76.2.0', '76.76.10.0'],
    'DNS.Watch': ['84.200.69.80', '84.200.70.40'],
    'DYN': ['216.146.35.35', '216.146.36.36'],
    'Electro' : ['78.157.42.100', '78.157.42.101'],
    'FreeDNS': ['37.235.1.174', '37.235.1.177'],
    'Google public' : ['8.8.8.8', '8.8.4.4'],
    'Level3': ['209.244.0.3', '209.244.0.4'],
    'Neustar': ['156.154.70.22', '156.154.71.22'],
    'NextDNS': ['45.90.28.0', '45.90.30.0'],
    'OpenDNS' : ['208.67.222.222', '208.67.220.220'],
    'OpenNIC': ['216.87.84.211', '23.90.4.6'],
    'Pishgaman': ['5.202.100.100', '5.202.100.101'],
    'Quad9' : ['9.9.9.9', '149.112.112.112'],
    'Radar': ['10.202.10.10', '10.202.10.11'],
    'Safe': ['195.46.39.39', '195.46.39.40'],
    'Shecan' : ['178.22.122.100', '185.51.200.2'],
    'Shelter public': ['94.103.125.157', '94.103.125.158'],
    'SmartViper': ['208.76.50.50', '208.76.51.51'],
    'Verisign public': ['64.6.64.6', '64.6.65.6'],
    'Yandex (Basic)': ['77.88.8.8', '77.88.8.1'],
    'Yandex (Family)': ['77.88.8.7', '77.88.8.3'],
    'Yandex (Safe)': ['77.88.8.88', '77.88.8.2']
    }
system, node, release, version, machine, cpu = platform.uname()
print('Welcome to DNS changer')
valid_networks = []
match system:
    case 'Windows':  # Windows section
        cnc = subprocess.run(['ipconfig', '/all'], capture_output=True).stdout.decode()  # 'cnc' -> cmd network check
        cenf = list(re.findall('Ethernet adapter (.*):', cnc))  # 'cenf' -> cmd ethernet network find
        cwnf = list(re.findall('Wireless LAN adapter (.*):', cnc))  # 'cwnf' -> cmd wifi network find
        dl = 0
        dl_head = ('     ' + 42 * '_')  # 'dl_head' -> Dns list header
        dl_body = ('     |' + 40 * '-' + '|')  # 'dl_body' -> Dns list body
        dl_foot = ('     |>>>>>>>>> created by D4rk $ide <<<<<<<<<|' + '\n' +'     ' + 42 * '-')  # 'dl_foot' -> Dns list footer
        print(dl_head, '     |  DNS server name  |  DNS server number |', dl_body, sep='\n')
        dls = []
        valid_codes = ['f', 'd']
        for dns in dns_dict:
            dl += 1
            dn = (int(abs(float(len(dns) - 19) // 2)) * ' ' + f'{dns}' + int(abs(float(len(dns) - 19) / 2)) * ' ')
            dc = (int(abs(float(len(str(dl)) - 17) // 2)) * ' ' + f'({dl})' + int(abs(float(len(str(dl)) - 19) / 2)) * ' ')
            print('     |' + dn + '|' + dc + '|', dl_body, sep='\n')
            dls.append(dns)
        for i in range(1, dl + 1):
            valid_codes.append(str(i))
        DHCP = (int(abs(float(len('DHCP') - 19) // 2)) * ' ' + 'DHCP' + int(abs(float(len('DHCP') - 19) / 2)) * ' ')
        Flush = (int(abs(float(len('flush DNS') - 19) // 2)) * ' ' + 'flush DNS' + int(abs(float(len('flush DNS') - 19) / 2)) * ' ')
        print('     |' + DHCP + '|        (d)         |', dl_body, '     |' + Flush + '|        (f)         |', dl_body, dl_foot, sep='\n')
        match release:
            case '7':
                def dns_loader_win7(dnscode, dnsname):
                    cpds = os.system(f'netsh interface ipv4 set dns "{nl[int(ns) - 1]}" static {dns_dict[dnscode][0]}')  # 'cpds' -> cmd primary DNS set
                    csds = os.system(f'netsh interface ipv4 add dns "{nl[int(ns) - 1]}" {dns_dict[dnscode][1]} index=2')  # 'csds' -> cmd secondary DNS set
                    print(f"You are now using the '{dnsname}' DNS \nGood luck!")
                    time.sleep(2)
                    os.system('cls')
                while True:
                    sd = input('select dns: ')  # 'sd' -> selected DNS
                    if sd in valid_codes:
                        match sd:
                            case 'f':
                                cfd = subprocess.run(['ipconfig', '/flushdns'])  # 'cfd' -> Cmd flush DNS
                                time.sleep(2)
                                os.system('cls')
                            case 'd':
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
                                for i in range(1, len(nl) + 1):
                                    valid_networks.append(str(i))
                                while True:
                                    ns = input('select your network: ')  # 'ns' -> Network select
                                    if ns in valid_networks:
                                        cpds = os.system(f'netsh interface ipv4 set dns "{nl[int(ns) - 1]}" dhcp')
                                        print(f"Now your DNS set on Dynamic Host Configuration Protocol(DHCP) \nGood luck!")
                                        time.sleep(2)
                                        os.system('cls')
                                        break
                                    else:
                                        print('Please enter a valid network code.')
                            case _:
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
                                for i in range(1, len(nl) + 1):
                                    valid_networks.append(str(i))
                                while True:
                                    ns = input('select your network: ')  # 'ns' -> Network select
                                    if ns in valid_networks:
                                        dns_loader_win7((dls[int(sd) - 1]), dls[int(sd) - 1])
                                        break
                                    else:
                                        print('Please enter a valid network code.')
                        break
                    else:
                        print('Please enter a valid DNS code.')
            case _:
                def dns_loader_windows(dnscode, dnsname):
                    subprocess.run(['netsh', 'interface', 'ip', 'set', 'dns', f'name="{nl[int(ns) - 1]}"', 'static', dns_dict[dnscode][0]])
                    subprocess.run(['netsh', 'interface', 'ip', 'add', 'dns', f'name="{nl[int(ns) - 1]}"', dns_dict[dnscode][1], 'index=2'])
                    print(f"You are now using the '{dnsname}' DNS \nGood luck!")
                    time.sleep(2)
                    os.system('cls')
                while True:
                    sd = input('select dns: ')  # 'sd' -> selected DNS
                    if sd in valid_codes:
                        match sd:
                            case 'f':
                                cfd = subprocess.run(['ipconfig', '/flushdns'])  # 'cfd' -> Cmd flush DNS
                                time.sleep(2)
                                os.system('cls')
                            case 'd':
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
                                for i in range(1, len(nl) + 1):
                                    valid_networks.append(str(i))
                                while True:
                                    ns = input('select your network: ')  # 'ns' -> Network select
                                    if ns in valid_networks:
                                        cpds = subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dnsservers', f'name="{nl[int(ns) - 1]}"', 'source=dhcp'])
                                        print(f"Now your DNS set on Dynamic Host Configuration Protocol(DHCP) \nGood luck!")
                                        time.sleep(2)
                                        os.system('cls')
                                        break
                                    else:
                                        print('Please enter a valid network code.')
                            case _:
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
                                for i in range(1, len(nl) + 1):
                                    valid_networks.append(str(i))
                                while True:
                                    ns = input('select your network: ')  # 'ns' -> Network select
                                    if ns in valid_networks:
                                        dns_loader_windows((dls[int(sd) - 1]), dls[int(sd) - 1])
                                        break
                                    else:
                                        print('Please enter a valid network code.')
                        break
                    else:
                        print('Please enter a valid DNS code.')
    case 'Linux':  # Linux section
        dl = 0
        dl_head = ('     ' + 42 * '_')  # 'dl_head' -> Dns list header
        dl_body = ('     |' + 40 * '-' + '|')  # 'dl_body' -> Dns list body
        dl_foot = ('     |>>>>>>>>> created by D4rk $ide <<<<<<<<<|' + '\n' +'     ' + 42 * '-')  # 'dl_foot' -> Dns list footer
        print(dl_head, '     |  DNS server name  |  DNS server number |', dl_body, sep='\n')
        dls = []
        valid_codes = ['d']
        for dns in dns_dict:
            dl += 1
            dn = (int(abs(float(len(dns) - 19) // 2)) * ' ' + f'{dns}' + int(abs(float(len(dns) - 19) / 2)) * ' ')
            dc = (int(abs(float(len(str(dl)) - 17) // 2)) * ' ' + f'({dl})' + int(abs(float(len(str(dl)) - 19) / 2)) * ' ')
            print('     |' + dn + '|' + dc + '|', dl_body, sep='\n')
            dls.append(dns)
        for i in range(1, dl + 1):
            valid_codes.append(str(i))
        DHCP = (int(abs(float(len('DHCP') - 19) // 2)) * ' ' + 'DHCP' + int(abs(float(len('DHCP') - 19) / 2)) * ' ')
        print('     |' + DHCP + '|        (d)         |', dl_body, dl_foot, sep='\n')
        def dns_loader_linux(dnscode):
            os.system(f'nmcli con mod {slicer} ipv4.dns {dns_dict[dnscode][0]}')
            os.system(f'nmcli con mod {slicer} +ipv4.dns {dns_dict[dnscode][1]}')
            os.system(f'nmcli con mod {slicer} ipv4.ignore-auto-dns yes')
            os.system(f'nmcli con down {slicer} && nmcli con up {slicer}')
        while True:
            sd = input('select dns: ')  # 'sd' -> selected DNS
            if sd in valid_codes:
                match sd:
                    case 'd':
                        net_names = []
                        net_types = []
                        net_devices = []
                        connections = str(subprocess.run(['nmcli', 'con', 'show'],capture_output=True).stdout).strip("b'").split('\\n')
                        dhcp_find0 = str(subprocess.run(['systemd-resolve', '--status'],capture_output=True).stdout).strip("b'").split('\\n')
                        for connection in range(1, len(connections) - 1):
                            net_names.append(str(connections[connection].split('  ')[0]))
                            net_types.append(str(connections[connection]).rstrip(' ').split('  ')[-2])
                            net_devices.append(str(connections[connection]).rstrip(' ').split('  ')[-1])
                        nl_head = ('    ' + 105 * '_')
                        nl_body = ('    |' + 103 * '-' + '|')
                        print(nl_head, '    |' + (18 * ' ') + 'Network name' + (18 * ' ') + '| Connection type |' + ' Connection device |' + ' Network number |', nl_body, sep='\n')
                        for i in range(len(net_names)):
                            nn = (int(abs(float(len(net_names[i]) - 48) // 2)) * ' ' + f'{net_names[i]}' + int(abs(float(len(net_names[i]) - 48) / 2)) * ' ')  # 'nn' -> Network name
                            nt = (int(abs(float(len(net_types[i]) - 17) // 2)) * ' ' + f'{net_types[i]}' + int(abs(float(len(net_types[i]) - 17) / 2)) * ' ')
                            nd = (int(abs(float(len(net_devices[i]) - 19) // 2)) * ' ' + f'{net_devices[i]}' + int(abs(float(len(net_devices[i]) - 19) / 2)) * ' ')
                            nc = (int(abs(float(len(str(i)) - 14) // 2)) * ' ' + f'({i + 1})' + int(abs(float(len(str(i)) - 14) / 2)) * ' ')
                            print('    |' + nn + '|' + nt + '|' + nd + '|' + nc + '|', nl_body, sep='\n')
                        for i in range(1, len(net_names) + 1):
                                    valid_networks.append(str(i))
                        while True:
                            ns = input('select your network: ')  # 'ns' -> Network select
                            if ns in valid_networks:
                                dhcp_find1 = str(dhcp_find0).find(net_devices[ns - 1])
                                slicer = net_names[ns - 1]
                                slicer = slicer.replace(' ', r'\ ')
                                os.system(f'nmcli con mod {slicer} ipv4.ignore-auto-dns no')
                                dhcp_choose = str(dhcp_find0)[dhcp_find1:dhcp_find1 + len(net_devices[ns - 1])]
                                os.system(f'nmcli con down {slicer} && nmcli con up {slicer}')
                                print(f"Your DNS has been restored to its original state.\nGood luck!")
                                time.sleep(2)
                                os.system('clear')
                                break
                            else:
                                print('Please enter a valid network code.')
                    case _:
                        net_names = []
                        net_types = []
                        net_devices = []
                        connections = str(subprocess.run(['nmcli', 'con', 'show'],capture_output=True).stdout).strip("b'").split('\\n')
                        for connection in range(1, len(connections) - 1):
                            net_names.append(str(connections[connection].split('  ')[0]))
                            net_types.append(str(connections[connection]).rstrip(' ').split('  ')[-2])
                            net_devices.append(str(connections[connection]).rstrip(' ').split('  ')[-1])
                        nl_head = ('    ' + 105 * '_')
                        nl_body = ('    |' + 103 * '-' + '|')
                        print(nl_head, '    |' + (18 * ' ') + 'Network name' + (18 * ' ') + '| Connection type |' + ' Connection device |' + ' Network number |', nl_body, sep='\n')
                        for i in range(len(net_names)):
                            nn = (int(abs(float(len(net_names[i]) - 48) // 2)) * ' ' + f'{net_names[i]}' + int(abs(float(len(net_names[i]) - 48) / 2)) * ' ')  # 'nn' -> Network name
                            nt = (int(abs(float(len(net_types[i]) - 17) // 2)) * ' ' + f'{net_types[i]}' + int(abs(float(len(net_types[i]) - 17) / 2)) * ' ')
                            nd = (int(abs(float(len(net_devices[i]) - 19) // 2)) * ' ' + f'{net_devices[i]}' + int(abs(float(len(net_devices[i]) - 19) / 2)) * ' ')
                            nc = (int(abs(float(len(str(i)) - 14) // 2)) * ' ' + f'({i + 1})' + int(abs(float(len(str(i)) - 14) / 2)) * ' ')
                            print('    |' + nn + '|' + nt + '|' + nd + '|' + nc + '|', nl_body, sep='\n')
                        for i in range(1, len(net_names) + 1):
                                    valid_networks.append(str(i))
                        while True:
                            ns = input('select your network: ')  # 'ns' -> Network select
                            if ns in valid_networks:
                                slicer = net_names[ns - 1]
                                slicer = slicer.replace(' ', r'\ ')
                                dns_loader_linux((dls[int(sd) - 1]))
                                print(f"You are now using the '{(dls[int(sd) - 1])}' DNS \nGood luck!")
                                time.sleep(2)
                                os.system('clear')
                                break
                            else:
                                print('Please enter a valid network code.')
                break
            else:
                print('Please enter a valid code.')
    case _:
        print('Failed to detect os!')