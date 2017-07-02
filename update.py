from bs4 import BeautifulSoup
from mod import EnemyModDrop
import requests
import os
r = requests.get('http://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
soup = BeautifulSoup(r.content.decode(), "html5lib")
mod_locations = soup.find_all(id='modLocations')[0].next_sibling
mod_locations = next(mod_locations.children).contents
i = -1
mods = {}
print([x for x in mod_locations[:5]])
for element in mod_locations:
    print(element.name, len(element.contents))
    if 'class' in element and element['class'] == 'blank-row':
        continue 
    if element.contents[0].name == 'th' and len(element.contents) == 1:
        print('boop')
        current_element = element.string
        mods[current_element] = []
    elif len(element.contents) == 3 and not element.contents[0].name == 'th':
        mods[current_element].append(EnemyModDrop(
            element.contents[0].string,
            float(element.contents[1].string[:-1]),
            float(element.contents[2].string.split()[-1][1:-2]),
            ' '.join(element.contents[2].string.split()[:-1])
        ))
if not os.path.exists('mods.db'): open('mods.db', 'x').close()

open('mods.db', 'w').write(repr(mods))
