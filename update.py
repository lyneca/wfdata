#!/usr/bin/python3
from bs4 import BeautifulSoup
from mod import EnemyModDrop, MissionDrop
from relic import Relic, RelicDrop
from mission import Mission
from hashlib import sha256
from datetime import datetime
import re
import requests
import sys
import os

def dprint(*args, **kwargs):
    if __name__ == '__main__':
        print(*args, **kwargs)

def save_mods(soup):
    dprint('Extracting mods and blueprints... ', end='')
    sys.stdout.flush()
    mod_locations = []
    rewardsTableNames = ['modLocations', 'blueprintLocations']
    for name in rewardsTableNames:
        mod_locations += next(soup.find_all(id=name)[0].next_sibling.children).contents
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
    dprint('Writing to file...                ', end='')
    sys.stdout.flush()

    if not os.path.exists('data/mods.db'): open('data/mods.db', 'x').close()
    open('data/mods.db', 'w').write(repr(mods))
    dprint('done.')

def save_missions(soup):
    dprint('Extracting missions...            ', end='')
    sys.stdout.flush()
    locations = []
    rewardsTableNames = ['missionRewards'] # 'relicRewards', 'keyRewards', 'transientRewards', 'sortieRewards'
    for name in rewardsTableNames:
        locations += next(soup.find_all(id=name)[0].next_sibling.children).contents
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
            event = False
            mission = current_element
            if mission.split()[0] == "Event:":
                event = True
                mission = ' '.join(mission.split()[1:])
            mission = Mission(
                    mission.split('/')[0],
                    mission.split('(')[0].split('/')[1][:-1],
                    mission.split()[1][1:-1],
                    event
            )
            missions.append(MissionDrop(
                mission,
                element.contents[0].string,
                rotation,
                float(element.contents[1].string.split()[-1][1:-2])
            ))
    dprint('done.')
    dprint('Writing to file...                ', end='')
    sys.stdout.flush()

    if not os.path.exists('data/missions.db'): open('data/missions.db', 'x').close()
    open('data/missions.db', 'w').write(repr(missions))
    dprint('done.')

def save_relics(soup):
    dprint('Extracting relics... ', end='')
    sys.stdout.flush()
    locations = soup.find_all(id='relicRewards')[0].next_sibling
    locations = next(locations.children).contents
    missions = []
    for element in locations:
        if 'class' in element and element['class'] == 'blank-row':
            continue 
        if element.contents[0].name == 'th' and len(element.contents) == 1:
            current_element = element.string
        elif len(element.contents) == 2 and not element.contents[0].name == 'th':
            relics.append(RelicDrop(
                mission,
                element.contents[0].string,
                rotation,
                float(element.contents[1].string.split()[-1][1:-2])
            ))
    dprint('done.')
    dprint('Writing to file...     ', end='')
    sys.stdout.flush()

def update():
    dprint("Starting update. This might take a while; we're parsing a lot of HTML here.")
    dprint('Downloading page...               ', end='')
    sys.stdout.flush()
    r = requests.get('http://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
    dprint('done.')
    
    if not os.path.exists('data/backups'):
        os.makedirs('data/backups')
    
    if os.path.exists('data/latest_hash.sha'):
        last_hash = open('data/latest_hash.sha').read()
        if sha256(r.content).hexdigest() == last_hash:
            dprint("No change since last update.")
            dprint("Finished.")
            return
    
    today = datetime.now().isoformat()
    if not os.path.exists(f'data/backups/{today}.html'):
        open(f'data/backups/{today}.html', 'x').close()
    open(f'data/backups/{today}.html', 'w').write(r.content.decode())

    if not os.path.exists('data/latest_hash.sha'): open('data/latest_hash.sha', 'x').close()
    open('data/latest_hash.sha', 'w').write(sha256(r.content).hexdigest())

    dprint('Parsing...                        ', end='')
    sys.stdout.flush()
    soup = BeautifulSoup(r.content.decode(), "html5lib")
    dprint('done.')

    # save_mods(soup)
    save_missions(soup)

    dprint('Finished.')

if __name__ == '__main__':
    update()
