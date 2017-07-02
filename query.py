from mod import EnemyModDrop, MissionDrop

from fuzzywuzzy import process
mods = eval(open('data/mods.db').read())
missions = eval(open('data/missions.db').read())
item_names = list(set([x.name for x in mods] + [x.name for x in missions]))
while True:
    name = process.extractOne(input('> '), item_names)[0]
    print(f"Interpreting as \"{name}\"")
    m = [x for x in mods if x.name == name] + \
        [x for x in missions if x.name == name]
    m.sort(key=lambda x: x.total_chance, reverse=True)
    for d in m:
        print(d)
