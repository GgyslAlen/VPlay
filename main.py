import cv2
import sys
import pygame
import screeninfo


def play(filename):
    cap = cv2.VideoCapture(filename)
    success, img = cap.read()
    screen = screeninfo.get_monitors()[0]
    width, height = screen.width, screen.height
    resolution = (img.shape[0], img.shape[1])
    wn = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    while success:
        clock.tick(60)
        success, img = cap.read()
        img = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                success, img = cap.read()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    success = False
        wn.blit(pygame.image.frombuffer(img.tobytes(), (width, height), "RGB"), (0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    file_name = sys.argv[1]
    play(file_name)
