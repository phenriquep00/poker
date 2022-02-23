import pygame as pg


class Slider:
    def __init__(self, x, y, w, h):
        self.circle_x = x
        self.value = 0
        self.sliderRect = pg.Rect(x, y, w, h)

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), self.sliderRect)
        pg.draw.circle(screen, (152, 240, 255), (self.circle_x, (self.sliderRect.h / 2 + self.sliderRect.y)),
                       self.sliderRect.h * 1.5)

    def get_value(self):
        return self.value

    def set_value(self, num):
        self.value = num

    def update_value(self, x):
        if x < self.sliderRect.x:
            self.value = 0
        elif x > self.sliderRect.x + self.sliderRect.w:
            self.value = 100
        else:
            self.value = int((x - self.sliderRect.x) / float(self.sliderRect.w) * 100)

    def on_slider(self, x, y):
        if self.on_slider_hold(x, y) or self.sliderRect.x <= x <= self.sliderRect.x + self.sliderRect.w and \
                self.sliderRect.y <= y <= self.sliderRect.y + self.sliderRect.h:
            return True
        else:
            return False

    def on_slider_hold(self, x, y):
        if ((x - self.circle_x) * (x - self.circle_x) + (y - (self.sliderRect.y + self.sliderRect.h / 2))
            * (y - (self.sliderRect.y + self.sliderRect.h / 2)))\
               <= (self.sliderRect.h * 1.5) * (self.sliderRect.h * 1.5):
            return True
        else:
            return False

    def handle_event(self, screen, x):
        if x < self.sliderRect.x:
            self.circle_x = self.sliderRect.x
        elif x > self.sliderRect.x + self.sliderRect.w:
            self.circle_x = self.sliderRect.x + self.sliderRect.w
        else:
            self.circle_x = x
        self.draw(screen)
        self.update_value(x)

# def bet_animate(window, original_pos):
#     # TODO: create a chip image and moveit from the punter's chips to the bet chip img at (405, 350)
#     pass
