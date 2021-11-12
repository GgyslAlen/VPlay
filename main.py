import sys
import pygame
import cv2


def play(filename):
    import cv2
    import pygame

    cap = cv2.VideoCapture(filename)
    success, img = cap.read()
    shape = img.shape[1::-1]
    wn = pygame.display.set_mode((64, 64), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    while success:
        clock.tick(60)
        success, img = cap.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                success = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    success = False
        wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    file_name = r"E:\\test_64_64.mp4"
    window_name = "window"
    play(file_name)
