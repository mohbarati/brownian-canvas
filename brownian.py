from random import random as rd
import pygame

pygame.init()
width, height = 900, 900  # size of screen
x, y = width // 2, height // 2  # initial position of the ball
j = 0
# Set up the drawing window
screen = pygame.display.set_mode([width, height])
alpha = 100  # time step
straight_tick = 1000  # How many ticks the object moves with given random speed
hold_tick = 100  # How many circles to be kept on the screen
flag = False
r = 10  # radius of the circles


def color():
    """Generate a color for the circles randomly.

    Returns:
        tuple: a color in the corm (r,g,b)
    """
    c = (int(255 * rd()), int(255 * rd()), int(255 * rd()))
    return c


# preallocating points to be kept on the screen
points = [None] * hold_tick

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keeping speed of the balls the same for straight_tick number of ticks
    if j % straight_tick == 0:
        c = color()  # update color when the direction chantges
        # random speeds
        vx = 0.5 - rd()
        vy = 0.5 - rd()

    # wall collision detection
    if x + vx * alpha <= r or x + vx * alpha >= width - r:
        vx = -vx
    if y + vy * alpha <= r or y + vy * alpha >= height - r:
        vy = -vy

    # updating the position of the circle
    x += vx * alpha
    y += vy * alpha

    points[j % hold_tick] = (x, y)  # keeping positions in hold_tick
    j += 1  # counting frames

    # making sure hold_tick number of circles are drawn before erasing starts
    if j == hold_tick:
        flag = True

    if flag:
        # erase one circle (from the beginning of the "points" list)
        pygame.draw.circle(screen, (0, 0, 0), points[j % hold_tick], r)
    # Draw a circle
    pygame.draw.circle(screen, c, (x, y), r)
    # update the display
    pygame.display.update()
# Done! Time to quit.
pygame.quit()
