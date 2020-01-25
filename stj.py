"""
1/25/20
Made in a few hours cuz I was sad. 
This project was just to fill time. I know it's not good.

Make sure you have python3 and pygame, then run it with
    > python3 stj.py
- Typing shows up on screen to a certain character limit
- "tab" changes image and music and also removes text
- "enter" removes your text

"""

import pygame # import pygame module in this program 
import random 
import os
import eztext
import sys
from pygame.locals import *
from my_modules import *

pygame.init() # activate/initiate the pygame library 
black = (0, 0, 0)

# Specifying the width and height
w = 1021
h = 654
  
# Creating  display surface object with specified width/height
screen = pygame.display.set_mode((w, h)) 
pygame.display.set_caption('Sadness Trance Journal') # Window name

# Getting initial song and image then loading them
image_name = get_rand_image()
song_name = get_rand_song()
pygame.mixer.music.load('./songs/' + song_name)
image = pygame.image.load('./images/' + image_name)
pygame.mixer.music.play(-1) # Start playing the song


reminder = "You will come back from this..."
pygame.font.init() # Initializing the pygame font
myfont = pygame.font.SysFont('Courier', 40)
text_message = myfont.render(reminder, False, (204, 0, 0))

# create the pygame clock to run in our loop
clock = pygame.time.Clock() 

# Creating the text box for user input
txtbx = eztext.Input(maxlength=50, color=(204, 0, 0), prompt='')
txtbx.set_pos(100,100)
# Game loop
while True : 
    clock.tick(30) # Running program at 30 fps

    screen.fill(black) # Color display surface white
    screen.blit(image, (0, 0)) # Copy image to display at (0,0)
    screen.blit(text_message,(0,0))
    txtbx.draw(screen)       # blit-ing txtbx on the sceen
    # Checking pygame events
    events = pygame.event.get()
    for event in events: 
        # If I click the "x" to close window, quit pygame and program
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit() 
        if event.type == pygame.KEYDOWN:
            # Hitting "tab" changes to a random images/songs in image/songs folders
            if event.key == pygame.K_TAB: 
                txtbx.value = '' # Also deletes text
                image_name = get_rand_image()
                song_name = get_rand_song()
                pygame.mixer.music.load('./songs/' + song_name)
                image = pygame.image.load('./images/' + image_name)
                screen.blit(image, (0, 0)) # Copy image to display at (0,0)
                pygame.mixer.music.play(-1)
            
            # Hitting "enter" removes text without changing song/image
            if event.key == pygame.K_RETURN:
                txtbx.value = ''


    
    txtbx.update(events)              # Updating textbox
    txtbx.draw(screen)                # blit-ing txtbx on the sceen
    pygame.display.update()           # Refreshing desplay

