from mod import EnemyModDrop, MissionDrop
from fuzzywuzzy import process

def dprint(*args, **kwargs):
    if __name__ == '__main__':
        print(*args, **kwargs)

mods = eval(open('data/mods.db').read())
missions = eval(open('data/missions.db').read())
item_names = list(set([x.name for x in mods] + [x.name for x in missions]))

def query(q):
    name = process.extractOne(q, item_names)[0]
    dprint(f"Interpreting as \"{name}\"")
    m = [x for x in mods if x.name == name] + \
        [x for x in missions if x.name == name]
    m.sort(key=lambda x: x.total_chance, reverse=True)
    return m

if __name__ == '__main__':
    global debug
    debug = True
    while True:
        for d in query(input('> ')):
            dprint(d)
        
