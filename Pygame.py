import pygame

# from pygame. local import *
pygame.init()
screen_info = pygame.display.Info()
# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 200, 255)fish_image = pygame.image.load("egggs.png")
fish_image = pygame.transform.smoothscale(fish_image,(100,100))

fish_rect = fish_image.get_rect()

fish_rect.center = (width//2,height//2)

speed=pygame.math.Vector2(5,5)


def movefish():
    fish_rect.move_ip(speed)

    if fish_rect.left < 0:
        speed[0] *= -1
    if fish_rect.right > width :
        speed[0] *= -1
    if fish_rect.top < (0):
        speed[1] *= -1
    if fish_rect.bottom > height:
        speed[1] *= -1
        egggs.png = pygame.transform.flip(fish_image,True,False,)
    if fish_rect.left<0 or fish_rect.right.width:
        speed[0] *= -1

def main():
    while True:
        clock.tick(60)
        movefish()
        screen.fill(color)
        screen.blit(fish_image,fish_rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
