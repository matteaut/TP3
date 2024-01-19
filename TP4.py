import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]  # Ajoutez plus de couleurs au besoin

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color(self.color))

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Circles Game")
        self.circle_list = []

    def setup(self):
        for _ in range(20):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            radius = 30
            color = random.choice(COLORS)
            circle = Circle(x, y, radius, color)
            self.circle_list.append(circle)

    def on_draw(self):
        arcade.start_render()
        for circle in self.circle_list:
            circle.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for circle in self.circle_list:
                if arcade.check_for_collision((x, y), (circle.x, circle.y, circle.radius)):
                    self.circle_list.remove(circle)
                    break
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            for circle in self.circle_list:
                if arcade.check_for_collision((x, y), (circle.x, circle.y, circle.radius)):
                    circle.color = random.choice(COLORS)
                    break

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
