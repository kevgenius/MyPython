for mac in MAC:
    if mac not in MAC_cisco:
        MAC_cisco.append(mac.replace(":", "."))
print(MAC_cisco)







