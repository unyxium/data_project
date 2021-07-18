import requests
import os
import time
from colorama import Fore, Style

LOCAL = os.path.dirname(os.path.realpath(__file__))

with open('loc6.txt') as f:  # Put all locations in to a list
    locations = [line.rstrip() for line in f]

lat = []
lon = []

count = 1

for loc in locations:
    print(loc)
    response = requests.get(
        f'https://nominatim.openstreetmap.org/search.php?q={loc}&format=jsonv2').json()

    if response == []:
        print(response)
        print(Fore.RED, 'failed')
        print(Style.RESET_ALL)
        lat.append('')
        lon.append('')
    else:
        coord1 = response[0]['lat']
        coord2 = response[0]['lon']
        lat.append(coord1)
        lon.append(coord2)
        print(coord1, coord2)
    print(f'count: {count}')
    count += 1
    time.sleep(1)

with open(LOCAL + '\lat.txt', 'w') as file:
    file.write(str(lat))
    print(Fore.GREEN, "saved lat")
    print(Style.RESET_ALL)

with open(LOCAL + '\lon.txt', 'w') as file:
    file.write(str(lon))
    print(Fore.GREEN, "saved lon")
    print(Style.RESET_ALL)
