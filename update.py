from bs4 import BeautifulSoup
from mod import EnemyModDrop, MissionDrop
import requests
import sys
import os
print("Starting update. This might take a while; we're parsing a lot of HTML here.")
print('Downloading page...    ', end='')
sys.stdout.flush()
r = requests.get('http://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
print('done.')
print('Parsing...             ', end='')
sys.stdout.flush()
soup = BeautifulSoup(r.content.decode(), "html5lib")
print('done.')

def save_mods():
    print('Extracting mod info... ', end='')
    sys.stdout.flush()
    mod_locations = soup.find_all(id='modLocations')[0].next_sibling
    mod_locations = next(mod_locations.children).contents
    i = -1
    mods = []
    for element in mod_locations:
        if 'class' in element and element['class'] == 'blank-row':
            continue 
        if element.contents[0].name == 'th' and len(element.contents) == 1:
            current_element = element.string
        elif len(element.contents) == 3 and not element.contents[0].name == 'th':
            mods.append(EnemyModDrop(
                element.contents[0].string,
                current_element,
                float(element.contents[1].string[:-1]),
                float(element.contents[2].string.split()[-1][1:-2]),
                ' '.join(element.contents[2].string.split()[:-1])
            ))
    print('done.')
    print('Writing to file...     ', end='')
    sys.stdout.flush()

    if not os.path.exists('data/mods.db'): open('data/mods.db', 'x').close()
    open('data/mods.db', 'w').write(repr(mods))
    print('done.')

def save_missions():
    print('Extracting mission info... ', end='')
    sys.stdout.flush()
    locations = soup.find_all(id='missionRewards')[0].next_sibling
    locations = next(locations.children).contents
    missions = []
    for element in locations:
        if 'class' in element and element['class'] == 'blank-row':
            continue 
        if element.contents[0].name == 'th' and len(element.contents) == 1:
            if element.contents[0].string.split()[0] == 'Rotation':
                rotation = element.string.split()[1]
            else:
                rotation = ''
                current_element = element.string
        elif len(element.contents) == 2 and not element.contents[0].name == 'th':
            missions.append(MissionDrop(
                current_element,
                element.contents[0].string,
                rotation,
                float(element.contents[1].string.split()[-1][1:-2])
            ))
    print('done.')
    print('Writing to file...     ', end='')
    sys.stdout.flush()

    if not os.path.exists('data/missions.db'): open('data/missions.db', 'x').close()
    open('data/missions.db', 'w').write(repr(missions))
    print('done.')

save_mods()
save_missions()
print('finished.')
