import arcade, enum, random


#créé par Tristan Matteau


class AttackType(enum.Enum):
    ROCK = 1
    PAPER= 2
    SCISSOR =  3

    COMPUTER = 4

class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.50
    ANIMATION_SPEED = 2.0
    def __init__(self, attack_type, pos_x, pos_y):
        super().__init__(center_x=pos_x, center_y=pos_y)

        self.attack_type = attack_type
        self.time_since_last_swap = 0.0
        self.animation_update_time = 1.0 / AttackAnimation.ANIMATION_SPEED

        self.nmb_of_swap = 0

        if self.attack_type == AttackType.ROCK:
            self.textures = [
                arcade.load_texture("assets/srock.png"),
                arcade.load_texture("assets/srock-attack.png"),
            ]
        elif self.attack_type == AttackType.PAPER:
            self.textures = [
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/spaper-attack.png"),
            ]
        elif self.attack_type == AttackType.SCISSOR:
            self.textures = [
                arcade.load_texture("assets/scissors.png"),
                arcade.load_texture("assets/scissors-close.png"),
            ]
        elif self.attack_type == AttackType.COMPUTER:
            self.textures = [
                arcade.load_texture("assets/srock.png"),
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/scissors.png"),
            ]
        self.scale = self.ATTACK_SCALE
        self.current_texture = 0
        self.set_texture(self.current_texture)

    def on_update(self, delta_time: float = 1 / 60):
       
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            self.nmb_of_swap += 1

            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0