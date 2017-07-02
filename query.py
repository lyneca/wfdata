from mod import EnemyModDrop
from fuzzywuzzy import process
mods = eval(open('data/mods.db').read())
while True:
    name = process.extractOne(input('> '), mods.keys())[0]
    print(f"Interpreting as \"{name}\"")
    m = mods[name]
    m.sort(key=lambda x: x.total_chance, reverse=True)
    for d in m:
        print(d)
