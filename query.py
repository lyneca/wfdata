#!/usr/bin/python3
from mod import EnemyModDrop, MissionDrop
from mission import Mission, GenericDropLocation
from fuzzywuzzy import process, fuzz, utils

def dprint(*args, **kwargs):
    if __name__ == '__main__':
        print(*args, **kwargs)

mods = eval(open('data/mods.db').read())
missions = eval(open('data/missions.db').read())
item_names = list(set([x.name for x in mods] + [x.dropped_by for x in mods] + [x.name for x in missions] + [x.dropped_by for x in missions]))

def query(q):
    nameScoreTuples = process.extractBests(q, item_names, utils.full_process, fuzz.WRatio, 25, 1)
    #Sort the results so the higher scored ones will be right above the console cursor
    nameScoreTuples.sort(key=lambda x: x[1])
    m = []
    for tuple in nameScoreTuples:
        name = tuple[0]
        m += [""]
        interpretingAsText = f"Interpreting as \"{name}\""
        mt = [x for x in mods if x.name == name] + \
            [x for x in missions if x.name == name]
        if len(mt) == 0:
            # Probably this is a mission or enemy name
            mt = [x for x in missions if x.dropped_by == name]
            if len(mt) == 0:
                # Probably this is an enemy name
                mt = [x for x in mods if x.dropped_by == name]
                # Sort by chance.
                mt.sort(key = lambda x: x.total_chance, reverse=True)
                if not len(mt) == 0:
                    interpretingAsText += " (enemy)"
            else:
                # Sort by rotation and chance.
                mt.sort(key = lambda x: 
                    x.total_chance - 100 * ((ord(x.rotation) - ord("A")) if len(x.rotation) > 0 else 0)
                , reverse=True)
                interpretingAsText += " (mission)"
            # Return the reverse name that contains the item instead of the mission/enemy name, the latter being the search query in this case
            mt = [x.reversedName() for x in mt]
        else:
            mt.sort(key=lambda x: x.total_chance, reverse=True)
            interpretingAsText += " (item)"
        m += [interpretingAsText]
        m = m + mt
    return m

if __name__ == '__main__':
    global debug
    debug = True
    while True:
        for d in query(input('> ')):
            dprint(d)
