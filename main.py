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
    | Windows | Coming soon...|
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