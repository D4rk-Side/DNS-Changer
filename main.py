import subprocess, re, os, time

cf_t = ('Cloudflare', '1.1.1.1', '1.0.0.1')
g_t = ('Google public', '8.8.8.8', '8.8.4.4')
od_t = ('OpenDNS', '208.67.222.222', '208.67.220.220')
sh_t = ('Shecan', '178.22.122.100', '185.51.200.2')
a_t = ('Azad(403)', '10.202.10.202', '10.202.10.102')
print('Welcome to DNS changer')
print("""DNS servers list:
     ________________________________________
     | DNS server name  | DNS server number |
     |--------------------------------------|
     |    Cloudflare    |       (1)         |
     |--------------------------------------|
     |      Google      |       (2)         |
     |--------------------------------------|
     |     OpenDNS      |       (3)         |
     |--------------------------------------|
     |      Shecan      |       (4)         |
     |--------------------------------------|
     |     Azad(403)    |       (5)         |
     |--------------------------------------|
     |>>>>>>>> created by D4rk $ide <<<<<<<<|
     ----------------------------------------
     """)
sd = input("select dns: ")  # 'sd' -> selected DNS
uo = input("""    ___________________________
    | OS name |   OS number   |
    |-------------------------|
    |  Linux  |      (1)      |
    |-------------------------|
    | Windows |      (2)      | 
    |-------------------------|
    |   Mac   | Coming soon...|
    |-------------------------|

select your os: """)  # 'uo' -> user os
if uo == "1":
    if sd == "1":
        os.system(f"echo nameserver {cf_t[1]} > /etc/resolv.conf && echo nameserver {cf_t[2]} >> /etc/resolv.conf")
    elif sd == "2":
        os.system(f"echo nameserver {g_t[1]} > /etc/resolv.conf && echo nameserver {g_t[2]} >> /etc/resolv.conf")
    elif sd == "3":
        os.system(f"echo nameserver {od_t[1]} > /etc/resolv.conf && echo nameserver {od_t[2]} >> /etc/resolv.conf")
    elif sd == "4":
        os.system(f"echo nameserver {sh_t[1]} > /etc/resolv.conf && echo nameserver {sh_t[2]} >> /etc/resolv.conf")
    elif sd == "5":
        os.system(f"echo nameserver {a_t[1]} > /etc/resolv.conf && echo nameserver {a_t[2]} >> /etc/resolv.conf")
    else:
        print("please type your dns server number.")
elif uo == "2":  # Windows section
    cnc = subprocess.run(['ipconfig', '/all'], capture_output=True).stdout.decode()  # 'cnc' -> cmd net check
    cnf = str(re.findall("Ethernet adapter (.*):", cnc))  # 'cnf' -> cmd net find
    cnbf = str(re.findall("Ethernet adapter Bluetooth (.*):", cnc))  # 'cnbf' -> cmd net bluetooth find
    es = str(re.findall('Ethernet', cnf))  # 'es' -> Ethernet select
    if sd == "1":
        cpds = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{es.strip("['']")}"', 'static',
             cf_t[1]])  # 'cpds' -> cmd primary DNS set
        csds = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{es.strip("['']")}"', cf_t[2],
             'index=2'])  # 'csds' -> cmd secondary DNS set
    elif sd == "2":
        cpds = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{es.strip("['']")}"', 'static', g_t[1]])
        csds = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{es.strip("['']")}"', g_t[2], 'index=2'])
    elif sd == "3":
        cpds = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{es.strip("['']")}"', 'static', od_t[1]])
        csds = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{es.strip("['']")}"', od_t[2], 'index=2'])
    elif sd == "4":
        cpds = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{es.strip("['']")}"', 'static', sh_t[1]])
        csds = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{es.strip("['']")}"', sh_t[2], 'index=2'])
    elif sd == "5":
        cpds = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{es.strip("['']")}"', 'static', a_t[1]])
        csds = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{es.strip("['']")}"', a_t[2], 'index=2'])
    else:
        print("please type your dns server number.")