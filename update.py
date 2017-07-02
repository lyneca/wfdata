from bs4 import BeautifulSoup
from mod import EnemyModDrop
import requests
import sys
import os
print('Downloading page...    ', end='')
sys.stdout.flush()
r = requests.get('http://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
print('done.')
print('Parsing...             ', end='')
sys.stdout.flush()
soup = BeautifulSoup(r.content.decode(), "html5lib")
print('done.')
print('Extracting mod info... ', end='')
sys.stdout.flush()
mod_locations = soup.find_all(id='modLocations')[0].next_sibling
mod_locations = next(mod_locations.children).contents
i = -1
mods = {}
for element in mod_locations:
    if 'class' in element and element['class'] == 'blank-row':
        continue 
    if element.contents[0].name == 'th' and len(element.contents) == 1:
        current_element = element.string
        mods[current_element] = []
    elif len(element.contents) == 3 and not element.contents[0].name == 'th':
        mods[current_element].append(EnemyModDrop(
            element.contents[0].string,
            float(element.contents[1].string[:-1]),
            float(element.contents[2].string.split()[-1][1:-2]),
            ' '.join(element.contents[2].string.split()[:-1])
        ))
print('done.')
print('Writing to file...     ', end='')
sys.stdout.flush()

if not os.path.exists('mods.db'): open('mods.db', 'x').close()
open('mods.db', 'w').write(repr(mods))

print('done.')
print('finished.')
