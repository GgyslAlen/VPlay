import cv2
import sys
import pygame


def play(filename):
    cap = cv2.VideoCapture(filename)
    success, img = cap.read()

    resolution = (img.shape[0], img.shape[1])
    wn = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    while success:
        clock.tick(60)
        success, img = cap.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                success, img = cap.read()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    success = False
        wn.blit(pygame.image.frombuffer(img.tobytes(), resolution, "BGR"), (0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    file_name = sys.argv[1]
    play(file_name)
