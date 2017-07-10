from mod import EnemyModDrop, MissionDrop
from fuzzywuzzy import process, fuzz, utils

def dprint(*args, **kwargs):
    if __name__ == '__main__':
        print(*args, **kwargs)

mods = eval(open('data/mods.db').read())
missions = eval(open('data/missions.db').read())
item_names = list(set([x.name for x in mods] + [x.name for x in missions]))

def query(q):
    nameScoreTuples = process.extractBests(q, item_names, utils.full_process, fuzz.WRatio, 25, 10)
    #Sort the results so the higher scored ones will be right above the console cursor
    nameScoreTuples.sort(key=lambda x: x[1])
    m = []
    for tuple in nameScoreTuples:
        name = tuple[0]
        m += ["", f"Interpreting as \"{name}\""]
        mt = [x for x in mods if x.name == name] + \
            [x for x in missions if x.name == name]
        mt.sort(key=lambda x: x.total_chance, reverse=True)
        m = m + mt
    return m

if __name__ == '__main__':
    global debug
    debug = True
    while True:
        for d in query(input('> ')):
            dprint(d)
