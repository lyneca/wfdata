from mod import EnemyModDrop
from fuzzywuzzy import process
mods = eval(open('mods.db').read())
while True:
    name = process.extractOne(input('> '), mods.keys())[0]
    print(f"Interpreting as \"{name}\"")
    m = mods[name]
    m.sort(key=lambda x: x.total_chance, reverse=True)
    for d in m:
        print(f"{d.name}: {d.total_chance:5.3}%")# (enemy drops mods {d.enemy_mod:5.3}% of the time, out of which {name} drops {d.mod_chance:5.3}% of the time.)")
