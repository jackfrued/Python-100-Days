from random import randint
from threading import Thread
from time import sleep

import pygame


class Color(object):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return r, g, b


class Car(object):

    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    def move(self):
        if self._x + 80 < 950:
            self._x += randint(1, 10)

    def draw(self, screen):
        pygame.draw.rect(screen, self._color,
                         (self._x, self._y, 80, 40), 0)


def main():

    class BackgroundTask(Thread):

        def run(self):
            while True:
                screen.fill(Color.GRAY)
                pygame.draw.line(screen, Color.BLACK, (130, 0), (130, 600), 4)
                pygame.draw.line(screen, Color.BLACK, (950, 0), (950, 600), 4)
                for car in cars:
                    car.draw(screen)
                pygame.display.flip()
                sleep(0.05)
                for car in cars:
                    car.move()

    cars = []
    for index in range(5):
        temp = Car(50, 50 + 120 * index, Color.random_color())
        cars.append(temp)
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    BackgroundTask(daemon=True).start()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


if __name__ == '__main__':
    main()
