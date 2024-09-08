import random

objects = {"names": ["brahim"], "nachName": ["abdelmoumen"],
           "ages": [19, 20], "live": ["casablanca", "dortmund", "kiel", "munich", "zurich", "strasbourg", "essen", "colone", "dusseldorf", "frankfurt", "stuttgart"], "komme aus": ["marokko"], "hobbys": ["poker spielen", "web entwickler", "Problemlösung", "Logik studieren ", "Geschichte", "videospeilen"]
           }


def get_value(par):
    value = objects[par][random.randint(0, len(objects[par]) - 1)]

    return value


print(
    f"hallo mein name ist {get_value('names')} und ich bin {get_value('ages')}, also komme ich aus {get_value('komme aus')} zurzeit lebe ich im {get_value('live')} mein leiblings hobbys sind {get_value('hobbys')} und {get_value('hobbys')}    ")
