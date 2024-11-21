import pygame


def play_song(song_name, start=0, loops=-1):
    pygame.mixer.music.load(f'Songs/{song_name}/song.mp3')
    pygame.mixer.music.play(loops=loops, start=start)


def stop_current():
    pygame.mixer.music.stop()


def pause_current():
    pygame.mixer.music.pause()


def resume_current():
    pygame.mixer.music.unpause()
