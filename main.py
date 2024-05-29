#créé par: Tristan Matteau 2024

import attack_animation, game_state, random, arcade

CHOICES = [attack_animation.AttackType.SCISSOR, attack_animation.AttackType.PAPER,attack_animation.AttackType.ROCK]
class MyGame(arcade.Window):
    def __init__(self):
        
        super().__init__(800,800,"TP5")
        self.reset_round()
        self.game_state=game_state.GameState.GAME_NOT_STARTED

        arcade.set_background_color(arcade.color.ROBIN_EGG_BLUE)
        self.pointage_player = 0
        self.pointage_computer = 0

        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(arcade.Sprite("assets\_faceBeard.png", scale = 0.4, center_x=200, center_y=400))
        self.sprite_list.append(arcade.Sprite("assets\compy.png", scale = 2, center_x=600, center_y=400))
        

        
    def draw_attacks(self):

        if self.animer_roche: self.rock.on_update()
    
        if self.animer_papier: self.paper.on_update()

        if self.animer_ciseaux: self.scissors.on_update()

        if self.animer_computer_attack: self.computer_attack.on_update()
        
        if self.draw_roche: self.rock.draw()
        
        if self.draw_papier: self.paper.draw()
        
        if self.draw_ciseaux: self.scissors.draw()

        if self.draw_computer_attack:self.computer_attack.draw()

    def validate_victory(self, player_attack, chosen_computer_attack):
        if player_attack == attack_animation.AttackType.ROCK and chosen_computer_attack == attack_animation.AttackType.SCISSOR:
            self.pointage_player += 1
            return "win"
        
        elif player_attack == attack_animation.AttackType.PAPER and chosen_computer_attack == attack_animation.AttackType.ROCK:
            self.pointage_player += 1
            return "win"
        
        elif player_attack == attack_animation.AttackType.SCISSOR and chosen_computer_attack == attack_animation.AttackType.PAPER:
            self.pointage_player += 1
            return "win"
        
        elif chosen_computer_attack == attack_animation.AttackType.ROCK and player_attack == attack_animation.AttackType.SCISSOR:
            self.pointage_computer += 1
            return "loss"
        
        elif chosen_computer_attack == attack_animation.AttackType.PAPER and player_attack == attack_animation.AttackType.ROCK:
            self.pointage_computer += 1
            return "loss"
        
        elif chosen_computer_attack == attack_animation.AttackType.SCISSOR and player_attack == attack_animation.AttackType.PAPER:
            self.pointage_computer += 1
            return "loss"
        
        return "draw"
    def on_update(self, delta_time):

        if self.computer_attack.nmb_of_swap == 6:
            self.animer_computer_attack = False

            self.computer_attack = attack_animation.AttackAnimation(attack_type=random.choice(CHOICES), pos_x=600, pos_y=600)

            self.result = self.validate_victory(self.chosen_attack.attack_type, self.computer_attack.attack_type)

            if self.pointage_player == 3 or self.pointage_computer == 3:
                self.game_state = game_state.GameState.GAME_OVER
            else:         
                self.game_state = game_state.GameState.ROUND_DONE

    def on_draw(self):

        arcade.start_render()

        if self.game_state == game_state.GameState.GAME_NOT_STARTED: 

            
            arcade.draw_text("  ROCHE, PAPIER, CISEAUX", 0, 750, arcade.color.GENERIC_VIRIDIAN,font_size=30, width=1)
            arcade.draw_text("  Appuyez ESPACE pour débuter la partie", 0, 510, arcade.color.GENERIC_VIRIDIAN,font_size=20, width=1)

        if self.game_state == game_state.GameState.ROUND_ACTIVE:

            self.draw_the_unmovable()
            arcade.draw_text("    Appuyez sur une attaque", 0, 710, arcade.color.GENERIC_VIRIDIAN,font_size=30, width=1)
            
            if self.draw_the_attacks: self.draw_attacks()

        if self.game_state == game_state.GameState.ROUND_DONE: 

            self.draw_the_unmovable()

            if self.draw_the_attacks: self.draw_attacks()

            if self.result == "win":
                arcade.draw_text("  Félicitation, vous avez gagné", 0, 750, arcade.color.GENERIC_VIRIDIAN,font_size=30, width=1)
                arcade.draw_text("  Appuyez sur ESPACE pour commencer une nouvelle round", 0, 710, arcade.color.GENERIC_VIRIDIAN,font_size=15, width=1)
            if self.result == "loss":
                arcade.draw_text("  GAME OVER  ", 0, 750, arcade.color.GENERIC_VIRIDIAN,font_size=30, width=1)
                arcade.draw_text("  Appuyez sur ESPACE pour commencer une nouvelle round", 0, 710, arcade.color.GENERIC_VIRIDIAN,font_size=15, width=1)
            if self.result == "draw":
                arcade.draw_text("  Bien essayer mais c'est une round nulle", 0, 750, arcade.color.GENERIC_VIRIDIAN,font_size=30, width=1)
                arcade.draw_text("  Appuyez sur ESPACE pour commencer une nouvelle round", 0, 710, arcade.color.GENERIC_VIRIDIAN,font_size=15, width=1)
                
        if self.game_state == game_state.GameState.GAME_OVER: 
            if self.pointage_player == 3: arcade.draw_text("  Félicitaion!, vous avez gagné la partie", 10, 400, arcade.color.GENERIC_VIRIDIAN,font_size=30, width=1)
            if self.pointage_computer == 3: arcade.draw_text("  GAME OVER  ", 10, 400, arcade.color.GENERIC_VIRIDIAN,font_size=30, width=1)
            arcade.draw_text("  Appuyer sur ESPACE pour deébuter une nouvelle partie", 10, 350, arcade.color.GENERIC_VIRIDIAN,font_size=20, width=1)





    def reset_round(self):
        self.rock = attack_animation.AttackAnimation(attack_animation.AttackType.ROCK, pos_x=100, pos_y=200)
        self.paper = attack_animation.AttackAnimation(attack_animation.AttackType.PAPER, pos_x=200, pos_y=200)
        self.scissors = attack_animation.AttackAnimation(attack_animation.AttackType.SCISSOR, pos_x=300, pos_y=200)

        self.computer_attack = attack_animation.AttackAnimation(attack_animation.AttackType.COMPUTER, pos_x=600, pos_y=600)
    
        self.game_state=game_state.GameState.ROUND_ACTIVE

        self.draw_the_attacks = True

        self.animer_roche = True
        self.animer_papier = True
        self.animer_ciseaux = True
        self.animer_computer_attack = False
        

        self.draw_roche = True
        self.draw_papier = True
        self.draw_ciseaux = True
        self.draw_computer_attack = False
        
        self.chosen_attack = None
        self.has_chosen_attack = False 
        self.result = None


        self.computer_attack = attack_animation.AttackAnimation(attack_animation.AttackType.COMPUTER, 600, 600)
    
    def draw_the_unmovable(self):
        self.sprite_list.draw()

        arcade.draw_rectangle_outline(100, 200, 75, 75, arcade.color.CYBER_YELLOW, 1)
        arcade.draw_rectangle_outline(200, 200, 75, 75, arcade.color.CYBER_YELLOW, 1)
        arcade.draw_rectangle_outline(300, 200, 75, 75, arcade.color.CYBER_YELLOW, 1)
    
        arcade.draw_rectangle_outline(600, 600, 75, 75, arcade.color.CYBER_YELLOW, 1)

        arcade.draw_text("Pointage de l'usager:%d"%self.pointage_player, 40, 110, arcade.color.GENERIC_VIRIDIAN,font_size=20, width=1)
        arcade.draw_text("Pointage de le bot:%d"%self.pointage_computer, 500, 110, arcade.color.GENERIC_VIRIDIAN,font_size=20, width=1)

    def on_key_press(self, symbol, modifiers):

        if symbol == 32 and self.game_state == game_state.GameState.GAME_NOT_STARTED:
            self.game_state = game_state.GameState.ROUND_ACTIVE
        if symbol == 32 and self.game_state == game_state.GameState.ROUND_DONE:
            self.game_state = game_state.GameState.ROUND_ACTIVE
            self.reset_round()
        if symbol == 32 and self.game_state == game_state.GameState.GAME_OVER:
            self.game_state = game_state.GameState.GAME_NOT_STARTED
            self.reset_round()
            self.pointage_computer = 0
            self.pointage_player = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.has_chosen_attack == False and self.game_state == game_state.GameState.ROUND_ACTIVE and (self.rock.collides_with_point((x, y)) or self.paper.collides_with_point((x, y)) or self.scissors.collides_with_point((x, y))):
            self.has_chosen_attack = True

            if self.rock.collides_with_point((x, y)):
                
                self.draw_papier = False
                self.draw_ciseaux = False
                
                self.animer_roche = False
                self.chosen_attack = self.rock

            elif self.paper.collides_with_point((x, y)):
                
                self.draw_roche = False
                self.draw_ciseaux = False

                self.animer_papier = False
                self.chosen_attack = self.paper

            elif self.scissors.collides_with_point((x, y)):
                self.draw_papier = False
                self.draw_roche = False

                self.animer_ciseaux = False
                self.chosen_attack = self.scissors
            self.draw_computer_attack = True
            self.animer_computer_attack = True
def main():
    mygame=MyGame()

    mygame.on_draw()

    arcade.run()

main()