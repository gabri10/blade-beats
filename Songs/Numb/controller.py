from random import randint

from Sprites.fruit import Fruit

side_chosen = None
delay = 0

bpm = 110

one_beat = round(60 / bpm * 1000)
half_beat = round(one_beat / 2)
quarter_beat = round(half_beat / 2)


def get_last_timestamp(dict):
    if dict:
        return max(dict.keys())
    else:
        return None


def pulse_camera_timestamps(bpm=110, beats=1000):
    beat_duration_ms = 60000 / bpm
    return [round(beat_duration_ms * i) for i in range(1, beats + 1)]


def level_increase_timestamps():
    return [delay + 13000, delay + 122000]


def chorus_timestamp():
    return (delay + 104000) / 1000


def last_timestamp():
    return get_last_timestamp(song())


def song():
    dict = {}

    dict.update(first_chorus(delay + 3800))
    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3 + half_beat))
    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3 + half_beat, 2))
    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3 + half_beat, 2))
    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3 + half_beat, 3))

    dict.update(singer_part_1(get_last_timestamp(dict) + one_beat))
    dict.update(singer_part_2(get_last_timestamp(dict) + one_beat + one_beat + half_beat))

    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict.update(singer_part_2(get_last_timestamp(dict) + half_beat))

    dict.update(singer_part_1(get_last_timestamp(dict) + one_beat + one_beat + half_beat))
    dict[get_last_timestamp(dict) + one_beat + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict.update(singer_part_2(get_last_timestamp(dict) + half_beat))
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict.update(singer_part_3(get_last_timestamp(dict) + half_beat))
    dict.update(background_singer(get_last_timestamp(dict) + one_beat))

    dict.update(singer_part_1(get_last_timestamp(dict) + one_beat + half_beat))
    dict.update(singer_part_3(get_last_timestamp(dict) + half_beat))
    dict.update(background_singer(get_last_timestamp(dict) + one_beat))

    dict[get_last_timestamp(dict) + one_beat * 2 + half_beat] = {
        'is_long': True,
        'health': half_beat / 1000,
        'double': True,
    }

    dict.update(numb(get_last_timestamp(dict) + one_beat + half_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))

    dict.update(numb(get_last_timestamp(dict) + one_beat + half_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))

    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))

    dict.update(singer_part_1(get_last_timestamp(dict) + one_beat))
    dict.update(singer_part_2(get_last_timestamp(dict) + one_beat + one_beat + half_beat))
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict.update(singer_part_2(get_last_timestamp(dict) + half_beat, 2))

    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict.update(singer_part_1(get_last_timestamp(dict) + half_beat))

    dict[get_last_timestamp(dict) + one_beat * 2] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict.update(singer_part_3(get_last_timestamp(dict) + one_beat * 2, 2))
    dict.update(background_singer(get_last_timestamp(dict) + one_beat + half_beat + quarter_beat))

    dict.update(singer_part_1(get_last_timestamp(dict) + one_beat + half_beat))
    dict.update(singer_part_3(get_last_timestamp(dict) + half_beat))
    dict.update(background_singer(get_last_timestamp(dict) + one_beat))

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
        'double': True,
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
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': True,
        'health': half_beat / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': True,
        'health': half_beat / 1000,
        'double': True,
    }

    dict.update(numb(get_last_timestamp(dict) + one_beat + half_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))

    dict.update(numb(get_last_timestamp(dict) + one_beat + half_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))

    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))
    dict.update(numb_complement(get_last_timestamp(dict) + one_beat))

    dict[get_last_timestamp(dict) + one_beat * 2 + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': True,
        'health': (one_beat + half_beat) / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat * 3] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': True,
        'health': (one_beat + half_beat) / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat * 2] = {
        'is_long': True,
        'health': (one_beat) / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat * 2] = {
        'is_long': True,
        'health': (one_beat) / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat * 2] = {
        'is_long': True,
        'health': (one_beat) / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat + half_beat] = {
        'is_long': True,
        'health': (one_beat + half_beat) / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict[get_last_timestamp(dict) + one_beat * 3] = {
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
        'is_long': True,
        'health': (one_beat * 2 + half_beat) / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict[get_last_timestamp(dict) + one_beat * 3 + half_beat + quarter_beat] = {
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
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': True,
        'health': half_beat / 1000,
        'double': False,
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
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
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
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': True,
        'health': one_beat * 3 / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict[get_last_timestamp(dict) + one_beat * 4 + half_beat] = {
        'is_long': True,
        'health': half_beat / 1000,
        'double': True,
    }

    dict.update(numb(get_last_timestamp(dict) + one_beat + half_beat))

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
    dict[get_last_timestamp(dict) + one_beat] = {
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
        'is_long': True,
        'health': half_beat / 1000,
        'double': False,
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

    dict.update(first_chorus(get_last_timestamp(dict) + one_beat))
    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3 + half_beat))

    dict[get_last_timestamp(dict) + one_beat * 3 + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    return dict


def first_chorus(timestamp, variation=1):
    dict = {}

    dict[timestamp] = {
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
        'double': variation != 1,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    if variation != 3:
        dict[get_last_timestamp(dict) + (one_beat + half_beat)] = {
            'is_long': False,
            'health': 1,
            'double': variation != 1,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

        dict[get_last_timestamp(dict) + (one_beat + half_beat)] = {
            'is_long': False,
            'health': 1,
            'double': variation != 1,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    return dict


def singer_part_1(timestamp, variation=1):
    dict = {}

    dict[timestamp] = {
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
        'is_long': True,
        'health': (half_beat / 1000),
        'double': False,
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

    return dict


def singer_part_2(timestamp, variation=1):
    dict = {}

    dict[timestamp] = {
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
        'is_long': True,
        'health': half_beat / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': 'Left' if side_chosen == 'Right' else 'Right'
    }
    if variation == 2:
        dict[get_last_timestamp(dict) + one_beat] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': 'Left' if side_chosen == 'Right' else 'Right'
        }

    return dict


def singer_part_3(timestamp, variation=1):
    global side_chosen
    dict = {}

    dict[timestamp] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    if variation == 2:
        dict[timestamp] = {
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
        dict[get_last_timestamp(dict) + one_beat] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        side_chosen = Fruit.sides_to_spawn[randint(0, 1)]
        dict[get_last_timestamp(dict) + one_beat] = {
            'is_long': True,
            'health': one_beat * 5 / 1000,
            'double': False,
            'side_to_spawn': side_chosen
        }
    else:
        dict[get_last_timestamp(dict) + half_beat] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[get_last_timestamp(dict) + one_beat] = {
            'is_long': True,
            'health': half_beat / 1000,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[get_last_timestamp(dict) + one_beat] = {
            'is_long': True,
            'health': half_beat / 1000,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        dict[get_last_timestamp(dict) + one_beat] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
        side_chosen = Fruit.sides_to_spawn[randint(0, 1)]
        dict[get_last_timestamp(dict) + half_beat] = {
            'is_long': True,
            'health': one_beat * 5 / 1000,
            'double': False,
            'side_to_spawn': side_chosen
        }
    return dict


def background_singer(timestamp, variation=1):
    global side_chosen

    side_to_spawn = lambda: Fruit.sides_to_spawn[
        randint(0, 1)] if variation != 1 else 'Left' if side_chosen == 'Right' else 'Right'

    dict = {}

    dict[timestamp] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_to_spawn()
    }

    return dict


def numb(timestamp, variation=1):
    dict = {}

    dict[timestamp] = {
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
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
    }

    return dict


def numb_complement(timestamp, variation=1):
    dict = {}

    dict[timestamp] = {
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
    dict[get_last_timestamp(dict) + one_beat] = {
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
    return dict
