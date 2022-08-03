import arcade
import random
import os
import math

PLAYER_CHARACTER = 0
SPRITE_SCALING = 0.5

SPRITE_SCALING1 = .75
SPRITE_SCALING2 = .9

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COIN_SPEED = 0.5

SCREEN_TITLE = "Que Heist"

class Chest(arcade.Sprite):
    def update(self):
        self.center_x += 0
        self.center_y += 0

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Cop(arcade.Sprite):
    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * COIN_SPEED
            self.change_y = math.sin(angle) * COIN_SPEED

# The first screen players see
class StartView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BRIGHT_TURQUOISE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to Que Heist.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Would you like to play? ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Click to advance, or close to come back later.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100, arcade.color.GRAY, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)

# Displays instructions if Players choose to continue
class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Here are the Rules:", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Collect all 3 treasure chests before you can escape the maze.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Don't get caught by the zombie!",SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 70, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Click to advance to Character Selection.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200, arcade.color.GRAY, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # change GameView to name of Character Selection
        char_sel = CharSel()
        self.window.show_view(char_sel)

# Where the player chooses their character
class CharSel(arcade.View):
    def __init__(self):
        super().__init__()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        # Loads background image with all character options
        self.background = arcade.load_texture("../background.png")

    def on_show(self):
        # Required to start drawing
        arcade.start_render()
        # Draws background image loaded in __init__
        arcade.draw_texture_rectangle(400, 300, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    # Draws directions for Players to follow
    def on_draw(self):
        arcade.draw_text("Choose a character below:", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Press Up", SCREEN_WIDTH /5 - 40, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press Down", 2*SCREEN_WIDTH / 5-20, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press Left", 3*SCREEN_WIDTH / 5+20, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press Right", 4*SCREEN_WIDTH / 5+40, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150, arcade.color.GRAY, font_size=40, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        # updates the value of the variable globally
        global PLAYER_CHARACTER

        # Changes the value of PLAYER_CHARACTER depending on what key the player presses.
        # The last key pressed before advancing to the next screen corresponds the sprite used.
        if key == arcade.key.UP:
            PLAYER_CHARACTER = 1
        elif key == arcade.key.DOWN:
            PLAYER_CHARACTER = 2
        elif key == arcade.key.LEFT:
            PLAYER_CHARACTER = 3
        elif key == arcade.key.RIGHT:
            PLAYER_CHARACTER = 4

    # Advances to next screen after the Player selects a character
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

# Code for Game
class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.player_list = arcade.SpriteList()
        self.chest_list = arcade.SpriteList()
        self.cop_list = arcade.SpriteList()

        # Set up the player info
        # default player image if none selected
        self.player_sprite = Player("../images/monkey.png", SPRITE_SCALING)
        self.score = 0

        # Chooses corresponding sprite to selection made in Character Selection screen
        if PLAYER_CHARACTER == 1:
            self.player_sprite = arcade.Sprite("../images/character_femaleAdventurer_attack1.png", SPRITE_SCALING)
        elif PLAYER_CHARACTER == 2:
            self.player_sprite = arcade.Sprite("../images/gingerBread_NE.png", SPRITE_SCALING)
        elif PLAYER_CHARACTER == 3:
            self.player_sprite = arcade.Sprite("../images/monkey.png", SPRITE_SCALING)
        elif PLAYER_CHARACTER == 4:
            self.player_sprite = arcade.Sprite("../images/character_maleAdventurer_behindBack.png", SPRITE_SCALING)

        # Set up the player
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(1):
            # Create the cop instance
            cop = Cop("../images/character_zombie_attack0.png", SPRITE_SCALING)

            # Position the cop
            cop.center_x = 200
            cop.center_y = 200

            # Add the cop to the lists
            self.cop_list.append(cop)

        for i in range(3):
            # Create the chest instance
            chest = Chest("../images/chest_SE.png", SPRITE_SCALING)

            # Position the chest
            chest.center_x = random.randrange(SCREEN_WIDTH)
            chest.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the chest to the lists
            self.chest_list.append(chest)

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

        """ Set up the game and initialize the variables. """


    def on_draw(self):
        arcade.start_render()
        # Draw all the sprites.
        self.player_list.draw()
        self.cop_list.draw()
        self.chest_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 30, arcade.color.WHITE, 14)
        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_update(self, delta_time):

        # Call update on all sprites
        self.cop_list.update()
        self.chest_list.update()
        self.player_list.update()

        for cop in self.cop_list:
            cop.follow_sprite(self.player_sprite)

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.cop_list)
        hit_list2 = arcade.check_for_collision_with_list(self.player_sprite, self.chest_list)

        # Loop through each colliding sprite, remove it, and add to the
        # score.
        for cop in hit_list:
            cop.kill()


        for chest in hit_list2:
            chest.kill()
            self.score += 50
            self.window.total_score += 50

        # If we've collected all the games, then move to a "GAME_OVER"
        # state.
        if len(self.chest_list) == 0:
            game_over_view = GameOverWinView()
            self.window.set_mouse_visible(True)
            self.window.show_view(game_over_view)

        if len(self.cop_list) == 0:
            game_over_view = GameOverLoseView()
            self.window.set_mouse_visible(True)
            self.window.show_view(game_over_view)

    def on_mouse_motion(self, x, y, _dx, _dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y



class GameOverWinView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.APPLE_GREEN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You Escaped!", SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2+100, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         SCREEN_WIDTH/2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # change GameView to name of class for character selection
        game_view = CharSel()
        self.window.show_view(game_view)

class GameOverLoseView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_CARMINE_PINK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        arcade.draw_text("You have been caught!", 400, 500, arcade.color.BLACK, font_size=40, anchor_x="center")
        arcade.draw_text("Please try again.", SCREEN_WIDTH//2, SCREEN_HEIGHT//2, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Click to replay.", SCREEN_WIDTH//2, 200, arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = CharSel()
        self.window.show_view(game_view)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.total_score = 0
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()