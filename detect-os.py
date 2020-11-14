from netmiko import SSHDetect, ConnectHandler
from getpass import getpass

device = {
    'device_type': 'autodetect',
    'ip': 'x.x.x.x',
    'username': 'user',
    'password': getpass(),
}

guesser = SSHDetect(**device)
best_match = guesser.autodetect()
print(best_match)
print(guesser.potential_matches)

device["device_type"] = best_match

with ConnectHandler(**device) as connection:
    print(connection.find_prompt())
