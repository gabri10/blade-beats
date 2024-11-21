class GhostTown:
    def __init__(self):
        self.song = self.compose_song()
        self.increase_speed_timestamps = [45000, 83000]
        self.shake_camera_timestamps = [500 * i for i in range(1, 1001)]

    def guitar_riff(self, starting_tempo):
        dict = {}
        list = [starting_tempo + (i * 250) for i in range(0, 4)]

        for timestamp in list:
            dict[timestamp] = {
                'is_long': False,
                'health': 1,
            }

        dict[starting_tempo + 1000] = {
            'is_long': True,
            'health': 45,
        }

        return dict

    def compose_song(self):
        intial_delay = 170
        dict = {}

        dict[intial_delay] = {
            'is_long': True,
            'health': 45,
        }

        dict.update(self.guitar_riff(intial_delay + 900))
        dict.update(self.guitar_riff(intial_delay + 2900))
        dict.update(self.guitar_riff(intial_delay + 4900))

        dict[intial_delay + 6900] = {
            'is_long': False,
            'health': 1,
        }

        dict[intial_delay + 7400] = {
            'is_long': False,
            'health': 1,
        }

        dict.update(self.get_vocal_sequence(intial_delay + 7900, 1))
        dict.update(self.get_vocal_sequence(intial_delay + 15900, 1))
        dict.update(self.get_vocal_sequence(intial_delay + 23900, 2))
        dict.update(self.get_vocal_sequence(intial_delay + 31900, 1))

        dict[intial_delay + 39650] = {
            'is_long': False,
            'health': 1,
        }
        dict[intial_delay + 39900] = {
            'is_long': False,
            'health': 1,
        }

        dict[intial_delay + 40400] = {
            'is_long': False,
            'health': 1,
        }
        dict[intial_delay + 40900] = {
            'is_long': False,
            'health': 1,
        }

        dict.update(self.my_heart_is_a_ghost_town(intial_delay + 41400))
        dict.update(self.my_heart_is_a_ghost_town(intial_delay + 49400))

        dict.update(self.whisper_riff(intial_delay + 52400))
        dict.update(self.whisper_riff(intial_delay + 60400))
        dict.update(self.whisper_riff(intial_delay + 68400))
        dict.update(self.whisper_riff(intial_delay + 76400))

        dict.update(self.get_vocal_sequence(intial_delay + 85900, 1))
        dict.update(self.get_vocal_sequence(intial_delay + 93900, 1))
        dict.update(self.get_vocal_sequence(intial_delay + 101900, 2))
        dict.update(self.get_vocal_sequence(intial_delay + 109900, 1))

        dict[intial_delay + 117650] = {
            'is_long': False,
            'health': 1,
        }
        dict[intial_delay + 117900] = {
            'is_long': False,
            'health': 1,
        }

        dict[intial_delay + 118400] = {
            'is_long': False,
            'health': 1,
        }
        dict[intial_delay + 118900] = {
            'is_long': False,
            'health': 1,
        }

        dict.update(self.my_heart_is_a_ghost_town(intial_delay + 119400))
        dict.update(self.whisper_riff(intial_delay + 122400))

        return dict

    def get_vocal_sequence(self, start_time, variation=1):
        dict = {}

        dict[start_time] = {
            'is_long': True,
            'health': 15,
        }

        dict.update(self.guitar_riff(start_time + 750))
        dict.update(self.guitar_riff(start_time + 3000))

        final_sequence = {}
        match variation:
            case 1:
                final_sequence = {
                    start_time + 5000: {
                        'is_long': False,
                        'health': 1,
                    },
                    start_time + 5250: {
                        'is_long': False,
                        'health': 1,
                    },
                    start_time + 5500: {
                        'is_long': False,
                        'health': 1,
                    },
                    start_time + 5750: {
                        'is_long': False,
                        'health': 1,
                    },
                    start_time + 6250: {
                        'is_long': True,
                        'health': 45,
                    },
                }

            case 2:
                final_sequence = {
                    start_time + 5000: {
                        'is_long': True,
                        'health': 15,
                    },
                    start_time + 5500: {
                        'is_long': False,
                        'health': 1,
                    },
                    start_time + 5750: {
                        'is_long': False,
                        'health': 1,
                    },
                    start_time + 5900: {
                        'is_long': False,
                        'health': 1,
                    },
                    start_time + 6400: {
                        'is_long': True,
                        'health': 45,
                    },
                }
        dict.update(final_sequence)

        return dict

    def my_heart_is_a_ghost_town(self, starting_tempo):

        dict = {
            starting_tempo: {
                'is_long': True,
                'health': 15,
            },

            starting_tempo + 500: {
                'is_long': True,
                'health': 15,
            },

            starting_tempo + 1000: {
                'is_long': False,
                'health': 1,
            },

            starting_tempo + 1250: {
                'is_long': False,
                'health': 1,
            },

            starting_tempo + 1500: {
                'is_long': False,
                'health': 1,
            },

            starting_tempo + 2000: {
                'is_long': True,
                'health': 30,
            },
        }

        return dict

    def whisper_riff(self, staring_timestamp):
        return {
            staring_timestamp: {
                'is_long': False,
                'health': 1,
            },
            staring_timestamp + 500: {
                'is_long': False,
                'health': 1,
            },
            staring_timestamp + 750: {
                'is_long': False,
                'health': 1,
            },
            staring_timestamp + 1000: {
                'is_long': False,
                'health': 1,
            },
            staring_timestamp + 1250: {
                'is_long': False,
                'health': 1,
            },
            staring_timestamp + 1500: {
                'is_long': True,
                'health': 60,
            },
            staring_timestamp + 3000: {
                'is_long': False,
                'health': 1,
            },
            staring_timestamp + 3250: {
                'is_long': False,
                'health': 1,
            },
            staring_timestamp + 3500: {
                'is_long': True,
                'health': 60,
            },
            staring_timestamp + 5000: {
                'is_long': False,
                'health': 1,
            },
            staring_timestamp + 5250: {
                'is_long': False,
                'health': 1,
            },
            staring_timestamp + 5500: {
                'is_long': True,
                'health': 60,
            },
        }