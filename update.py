from bs4 import BeautifulSoup
from mod import EnemyModDrop, MissionDrop
from hashlib import sha256
from datetime import date
import requests
import sys
import os

def dprint(*args, **kwargs):
    if __name__ == '__main__':
        print(*args, **kwargs)

def save_mods(soup):
    dprint('Extracting mod info... ', end='')
    sys.stdout.flush()
    mod_locations = soup.find_all(id='modLocations')[0].next_sibling
    mod_locations = next(mod_locations.children).contents
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
    dprint('done.')
    dprint('Writing to file...     ', end='')
    sys.stdout.flush()

    if not os.path.exists('data/mods.db'): open('data/mods.db', 'x').close()
    open('data/mods.db', 'w').write(repr(mods))
    dprint('done.')

def save_missions(soup):
    dprint('Extracting mission info... ', end='')
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
    dprint('done.')
    dprint('Writing to file...     ', end='')
    sys.stdout.flush()

    if not os.path.exists('data/missions.db'): open('data/missions.db', 'x').close()
    open('data/missions.db', 'w').write(repr(missions))
    dprint('done.')

def update():
    dprint("Starting update. This might take a while; we're parsing a lot of HTML here.")
    dprint('Downloading page...    ', end='')
    sys.stdout.flush()
    r = requests.get('http://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
    dprint('done.')
    
    if os.path.exists('data/latest_hash.sha'):
        last_hash = open('data/latest_hash.sha').read()
        if sha256(r.content).hexdigest() == last_hash:
            dprint("No change since last update.")
            dprint("Finished.")
            return
    
    today = date.today().isoformat()
    if not os.path.exists(f'data/backups/{today}.html'):
        open(f'data/backups/{today}.html', 'x').close()
    open(f'data/backups/{today}.html', 'w').write(r.content.decode())

    if not os.path.exists('data/latest_hash.sha'): open('data/latest_hash.sha', 'x').close()
    open('data/latest_hash.sha', 'w').write(sha256(r.content).hexdigest())

    dprint('Parsing...             ', end='')
    sys.stdout.flush()
    soup = BeautifulSoup(r.content.decode(), "html5lib")
    dprint('done.')

    save_mods(soup)
    save_missions(soup)

    dprint('Finished.')

if __name__ == '__main__':
    update()
