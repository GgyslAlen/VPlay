import sys
import pygame
import cv2


def play(filename, windowname):
    cap = cv2.VideoCapture(filename)
    success, img = cap.read()
    wn = pygame.display.set_mode((64, 64), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    while success:
        clock.tick(60)
        success, img = cap.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                success = False
        wn.blit(pygame.image.frombuffer(img.tobytes(), (64, 64), "BGR"), (0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    file_name = r"E:\\test_64_64.mp4"
    window_name = "window"
    play(file_name, window_name)
