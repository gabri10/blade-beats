from random import randint

from Config.window_config import *
from Sprites.fruit import Fruit

side_chosen = None
delay = 0

bpm = 88

one_beat = round(60 / bpm * 1000)
half_beat = round(one_beat / 2)
quarter_beat = round(half_beat / 2)


def get_last_timestamp(dict):
    if dict:
        return max(dict.keys())
    else:
        return None

def pulse_camera_timestamps(bpm=88, beats=1000):
    beat_duration_ms = 60000 / bpm
    return [round(beat_duration_ms * i) for i in range(1, beats + 1)]

def level_increase_timestamps():
    return [delay + 29100, delay + 107300]

def chorus_timestamp():
    return (delay + 67900 - 100) / 1000

def last_timestamp():
    return get_last_timestamp(song())

def song():
    dict = {}

    dict[delay + 1100] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3))
    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3))
    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3))

    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict.update(vou_cacar_refrao(get_last_timestamp(dict) + one_beat))
    dict.update(apos_primeiro_refrao(get_last_timestamp(dict) + one_beat))
    dict.update(vou_cacar_refrao(get_last_timestamp(dict) + quarter_beat))


    return dict

def first_chorus(timestamp, variation=1):
    dict = {}

    dict[timestamp] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    return dict

def vou_cacar_refrao(timestamp, variation=1):
    dict = {}

    dict[timestamp] = { #VOOOUUUUU
        'is_long': True,
        'health': half_beat / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = { # UM MILHÃÃÃÃOOOOOOOOO
        'is_long': True,
        'health': one_beat / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = { # POR AIIIIIIIII
        'is_long': True,
        'health': one_beat / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = { # EEEUUUUU SÓ QUERO
        'is_long': True,
        'health': one_beat / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = { # AMAR (VOCEEEE)
        'is_long': True,
        'health': (half_beat + quarter_beat) / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = { # AMANHACEEEERRRR
        'is_long': True,
        'health': (one_beat + half_beat + quarter_beat) / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + (one_beat * 2) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = { # ACORDAARRR
        'is_long': True,
        'health': (one_beat * 2) / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + (one_beat * 3)] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    return dict

def apos_primeiro_refrao(timestamp, varation=1):
    dict = {}

    dict[timestamp] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    return dict

def apos_segundo_refrao(timestamp, variation=1):
        dict = {}

        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        return dict