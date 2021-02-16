from datetime import datetime
from time import time
from pygame import mixer


def play_music(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(1.0)
    mixer.music.play(-1)

    user_ip = input()
    user_ip = user_ip.lower()

    while True:
        if user_ip == stopper:
            mixer.music.stop()
            break


def log_to_file(msg):

    with open('logfile.txt', 'a') as log:
        log.write(f'[{datetime.now()}] - {msg} \n')


if __name__ == '__main__':
    init_water = init_eyes = init_exercise = time()

    water_time = 40*60
    eyes_time = 30*60
    exercise_time = 45*60

    while True:
        if time() - init_water > water_time:
            print('Time to drink water. Type "drank" to stop.')
            play_music('water.mp3', 'drank')
            init_water = time()
            log_to_file('Drank Water')

        if time() - init_eyes > eyes_time:
            print('Time for eyes exercise. Type "eydone" to stop.')
            play_music('eyes.mp3', 'eydone')
            init_eyes = time()
            log_to_file('Eyes Exercise Done')

        if time() - init_exercise > exercise_time:
            print('Time for exercise. Type "exdone" to stop.')
            play_music('physical.mp3', 'exdone')
            init_exercise = time()
            log_to_file('Physical Exercise Done')
