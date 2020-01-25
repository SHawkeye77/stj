# My created modules for this project
import random
import os 

def get_rand_image():
    # Returns name of random image file (non-hidden)
    image_name = random.choice(os.listdir("./images/"))
    while (image_name[0]=="."):
        image_name = random.choice(os.listdir("./images/"))
    return image_name

def get_rand_song():
    # Returns name of random mp3 file (non-hidden)
    song_name = random.choice(os.listdir("./songs/"))
    while (song_name[0]=="."):
        song_name = random.choice(os.listdir("./songs/"))
    return song_name