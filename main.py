import sys

from moviepy.editor import *
import pygame
from pygame import KEYDOWN, K_ESCAPE


def play(filename, windowname):
    pygame.display.set_caption(windowname)
    monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
    print(monitor_size)
    video = VideoFileClip(filename)
    video.resize(monitor_size).preview()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    file_name = r"/home/pi/test_64_64.mp4"
    window_name = "window"
    play(file_name, window_name)
