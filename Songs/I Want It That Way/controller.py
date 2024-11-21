from random import randint

from Config.window_config import *
from Sprites.fruit import Fruit

side_chosen = None
delay = 0


def pulse_camera_timestamps(bpm=99, beats=1000):
    beat_duration_ms = 60000 / bpm
    return [round(beat_duration_ms * i) for i in range(1, beats + 1)]


def level_increase_timestamps():
    return [delay + 29100, delay + 107300]


def chorus_timestamp():
    return (delay + 67900 - 100) / 1000


def last_timestamp():
    return delay + 150100


def song():
    dict = {
        delay + 3700: {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        },
        delay + 4000: {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        },
        delay + 4600: {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
    }
    dict.update(first_chorus(delay + 9700))
    dict.update(first_chorus(delay + 14500, 2))
    dict.update(first_chorus(delay + 19400))

    dict.update(i_want_it_that_way(delay + 24800, 4))

    dict.update(tell_me_why(delay + 29100))
    dict.update(aint_nothing_but(delay + 30300))

    dict.update(tell_me_why(delay + 33900))
    dict.update(aint_nothing_but(delay + 35100))

    dict.update(tell_me_why(delay + 38700, 2))

    dict.update(i_never_wanna_hear_you_say(delay + 39900))

    dict.update(i_want_it_that_way(delay + 44200))

    dict.update(first_chorus(delay + 48500))
    dict.update(first_chorus(delay + 53300, 2))
    dict.update(first_chorus(delay + 58100, 3))

    dict[delay + 63400] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }

    dict.update(i_want_it_that_way(delay + 63600, 2))

    dict.update(tell_me_why(delay + 67900))

    dict.update(aint_nothing_but(delay + 69100, 2))
    dict.update(tell_me_why(delay + 71801, 3))

    dict.update(aint_nothing_but(delay + 73900))
    dict.update(tell_me_why(delay + 77500, 2))

    dict.update(i_never_wanna_hear_you_say(delay + 78700))

    dict.update(i_want_it_that_way(delay + 83000))

    dict[delay + 87900] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 88200] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 88500] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 88800] = {
        'is_long': True,
        'health': FPS * 0.35,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }

    dict[delay + 89400] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 89700] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 90000] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 90300] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 90600] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 90600] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 90900] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 91200] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 91500] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 91800] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 92100] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }

    dict[delay + 92400] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 92550] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 92700] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 93000] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 93300] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 93600] = {
        'is_long': True,
        'health': FPS * 0.35,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 94200] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 94800] = {
        'is_long': True,
        'health': FPS * 0.35,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 95700] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 96000] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }

    dict[delay + 97300] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 97600] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 97900] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 98200] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 98500] = {
        'is_long': True,
        'health': FPS * 0.35,
        'double': True,
    }
    dict[delay + 99100] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }
    dict[delay + 99700] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 100000] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 100300] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 100600] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }
    dict[delay + 100900] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }

    dict[delay + 102100] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }
    dict[delay + 102400] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }
    dict[delay + 102700] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }
    dict[delay + 103000] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }
    dict[delay + 103300] = {
        'is_long': True,
        'health': FPS * 0.5,
        'double': True,
    }
    dict[delay + 104200] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }
    dict[delay + 104500] = {
        'is_long': True,
        'health': FPS * 2,
        'double': True,
        'checkpoint': True
    }

    dict.update(aint_nothing_but(delay + 107300, 3))
    dict.update(aint_nothing_but(delay + 112100, 3))

    dict.update(i_never_wanna_hear_you_say(delay + 116900, 2))

    dict[delay + 120800] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 121400] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }

    dict.update(i_want_it_that_way(delay + 122400, 3))

    dict.update(tell_me_why(delay + 126000, 4))
    dict.update(aint_nothing_but(delay + 127200, 4))
    dict.update(aint_nothing_but(delay + 132000, 2))
    dict.update(tell_me_why(delay + 135700, 2))

    dict.update(i_never_wanna_hear_you_say(delay + 136900, 2))

    dict.update(i_want_it_that_way(delay + 141200, 2))

    dict[delay + 145750] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 145900] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 147100] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 148000] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    dict[delay + 148900] = {
        'is_long': True,
        'health': FPS * 0.45,
        'double': True,
    }
    dict[delay + 150100] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }

    return dict


def first_chorus(timestamp, variation=1):
    dict = {}

    if variation == 4:
        dict[timestamp - 300] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }

        dict[timestamp + 300] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }

        dict[timestamp + 600] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }
        dict[timestamp + 900] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }
        dict[timestamp + 1200] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }
    if variation == 3:
        dict[timestamp - 300] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }

        dict[timestamp + 300] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }

        dict[timestamp + 600] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }
        dict[timestamp + 900] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }
        dict[timestamp + 1200] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
        }

    dict[timestamp] = {
        'is_long': False,
        'health': 1,
        'double': True if variation != 3 else False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)],
    }
    if variation != 3:
        dict[timestamp + 300] = {
            'is_long': True,
            'health': FPS,
            'double': True,
        }

    dict[timestamp + 2500] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[timestamp + 3100] = {
        'is_long': True,
        'health': FPS * 0.5,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[timestamp + 4000] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    if variation == 2:
        dict[timestamp + 4300] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
    return dict


def i_want_it_that_way(timestamp, variation=1):
    dict = {}

    if variation == 3:
        dict[timestamp] = {
            'is_long': True,
            'health': FPS * 0.8,
            'double': True,
        }
        dict[timestamp + 1200] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 1500] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 1800] = {
            'is_long': True,
            'health': FPS * 0.35,
            'double': True,
        }
        dict[timestamp + 2400] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 2700] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }


    else:
        dict[timestamp] = {
            'is_long': True,
            'health': FPS * 0.45,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 900] = {
            'is_long': True,
            'health': FPS * 0.45,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 1800] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        if variation == 2:
            dict[timestamp + 2400] = {
                'is_long': True,
                'health': FPS * 0.5,
                'double': True,
            }
        else:
            dict[timestamp + 2400] = {
                'is_long': True,
                'health': FPS * 0.35,
                'double': False,
                'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
            }
            dict[timestamp + 3000] = {
                'is_long': False,
                'health': 1,
                'double': True,
            }
        dict[timestamp + 3300] = {
            'is_long': False,
            'health': 1,
            'double': True,
            'checkpoint': variation == 4
        }

    return dict


def tell_me_why(timestamp, variation=1):
    global side_chosen
    dict = {}

    if variation == 3:
        dict[timestamp] = {
            'is_long': True,
            'health': FPS * 0.8,
            'double': False,
            'side_to_spawn': 'Left' if side_chosen != 'Left' else 'Right'
        }

        dict[timestamp + 900] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 1200] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
    else:
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 300] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        if variation == 4:
            side_chosen = Fruit.sides_to_spawn[randint(0, 1)]
            dict[timestamp + 600] = {
                'is_long': True,
                'health': FPS * 4.5,
                'double': False,
                'side_to_spawn': side_chosen
            }
        else:
            dict[timestamp + 600] = {
                'is_long': False,
                'health': 1,
                'double': False,
                'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
            }
    if variation == 1:
        dict[timestamp + 900] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    return dict


def aint_nothing_but(timestamp, variation=1):
    global side_chosen
    dict = {}

    if variation == 4:
        dict[timestamp] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': False,
            'side_to_spawn': 'Left' if side_chosen != 'Left' else 'Right'
        }
        dict[timestamp + 600] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': 'Left' if side_chosen != 'Left' else 'Right'
        }
        dict[timestamp + 900] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': 'Left' if side_chosen != 'Left' else 'Right'
        }
        dict[timestamp + 1200] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': 'Left' if side_chosen != 'Left' else 'Right'
        }
        dict[timestamp + 1500] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': 'Left' if side_chosen != 'Left' else 'Right'
        }
        dict[timestamp + 1800] = {
            'is_long': True,
            'health': FPS * 0.8,
            'double': False,
            'side_to_spawn': 'Left' if side_chosen != 'Left' else 'Right'
        }
        dict[timestamp + 2700] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': False,
            'side_to_spawn': 'Left' if side_chosen != 'Left' else 'Right'
        }
        return dict
    if variation == 3:
        dict[timestamp] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': True,
        }
        dict[timestamp + 1500] = {
            'is_long': False,
            'health': 1,
            'double': True,
        }
        dict[timestamp + 1800] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 2100] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 2400] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': True,
        }
        dict[timestamp + 3300] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': True,
        }
        pass
    else:
        dict[timestamp] = {
            'is_long': True,
            'health': FPS * 0.3,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

        dict[timestamp + 600] = {
            'is_long': False,
            'health': 1,
            'double': True,
        }

        dict[timestamp + 1200] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 1500] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 1800] = {
            'is_long': True,
            'health': FPS * 0.8,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
    dict[timestamp + 900] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }

    if variation == 2:
        side_chosen = Fruit.sides_to_spawn[randint(0, 1)]
        dict[timestamp + 2700] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': False,
            'side_to_spawn': side_chosen
        }

    elif variation == 1:
        dict[timestamp + 2700] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
    return dict


def i_never_wanna_hear_you_say(timestamp, variation=1):
    dict = {}

    if variation == 2:
        dict[timestamp] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': True,
        }
        dict[timestamp + 1050] = {
            'is_long': False,
            'health': 1,
            'double': True,
        }
        dict[timestamp + 1500] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 1800] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 2100] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 2400] = {
            'is_long': True,
            'health': FPS * 0.35,
            'double': True,
        }
        dict[timestamp + 3000] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 3300] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
    else:
        dict[timestamp] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 600] = {
            'is_long': False,
            'health': 1,
            'double': True,
        }
        dict[timestamp + 900] = {
            'is_long': False,
            'health': 1,
            'double': True,
        }
        dict[timestamp + 1200] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 1500] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 1800] = {
            'is_long': True,
            'health': FPS * 0.5,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 2400] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 2700] = {
            'is_long': True,
            'health': FPS * 0.35,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 3300] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[timestamp + 3400] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
    return dict
