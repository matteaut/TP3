#créé par: Tristan Matteau
#405

import arcade, random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLORS = [arcade.color.AFRICAN_VIOLET, arcade.color.ALABAMA_CRIMSON, arcade.color.ANDROID_GREEN, arcade.color.AIR_FORCE_BLUE, arcade.color.AIR_SUPERIORITY_BLUE, arcade.color.ATOMIC_TANGERINE, arcade.color.BLEU_DE_FRANCE, arcade.color.HOOKER_GREEN, arcade.color.LASER_LEMON, arcade.color.KOBE, arcade.color.LA_SALLE_GREEN]

class Circle:
    def __init__(self, position_x, position_y):
        self.x = position_x
        self.y = position_y
        self.radius = random.randint(10,20)
        self.color = random.choice(COLORS)
        self.change_x = random.randint(-5, 5)
        self.change_y = random.randint(-5, 5)
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
    def update(self):
        self.x += self.change_x

        if self.x > 800:
            self.change_x *= -1
        if self.x < 0:
            self.change_x *= -1

        self.y += self.change_y

        if self.y > 600:
            self.change_y *= -1
        if self.y < 0:
            self.change_y *= -1
class Rectangle:
    def __init__(self, position_x, position_y):
        self.x = position_x
        self.y = position_y
        self.longueur = random.randint(10, 20)
        self.largeur = random.randint(10, 20)
        self.color = random.choice(COLORS)
        self.change_x = random.randint(-5, 5)
        self.change_y = random.randint(-5, 5)

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.longueur, self.largeur, self.color)

    def update(self):
        self.x += self.change_x

        if self.x > 800:
            self.change_x *= -1
        if self.x < 0:
            self.change_x *= -1

        self.y += self.change_y

        if self.y > 600:
            self.change_y *= -1
        if self.y < 0:
            self.change_y *= -1



class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Circles and Rectangles Game")
        self.circle_and_rectangle_list = []

        arcade.set_background_color(arcade.color.AUROMETALSAURUS)
    def on_draw(self):
        arcade.start_render()

        for obj in self.circle_and_rectangle_list:
            obj.draw()
            obj.update()
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.circle_and_rectangle_list.append(Circle(position_x = x, position_y=y))
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.circle_and_rectangle_list.append(Rectangle(position_x=x, position_y=y))
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.on_draw()

    arcade.run()
main()

