import re

baris = int(input("Jumlah Baris : "))

IPv4Pattern = r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})2$'
IPv6Pattern = r'^([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4})2$'

hasil = []

def inputPerBaris(n):
    perBaris = input(f"Baris ke-{n} : ")
    cekIpV4 = re.match(IPv4Pattern, perBaris)
    cekIpV6 = re.match(IPv6Pattern, perBaris)
    if cekIpV4:
        hasil.append("IPv4")
    elif cekIpV6:
        hasil.append("IPv6")
    else: 
        hasil.append("Bukan IP Address")

for n in range(1, baris + 1):
    inputPerBaris(n)

for i in hasil:
    print(i)