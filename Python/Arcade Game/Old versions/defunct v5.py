import arcade
import random
import os

PLAYER_CHARACTER = 0
PLAYER_CHARACTER1 = 0
SPRITE_SCALING = 0.5

SPRITE_SCALING_COIN = 0.04
SPRITE_SCALING_BUMPER = 0.04
SPRITE_SCALING1 = 0.75
COIN_COUNT = 40
BUMPER_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Que Heist"

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
        arcade.draw_text("Collect as many treasure chests as possible.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("If you bump into each other, it's game over.",SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 70, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Good coins are +1. ", SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 + 40, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Bad coins are -1. Watch out for them.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 10, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Click to advance to Character Selection for Player 1.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200, arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # change GameView to name of Character Selection
        char_sel = CharSel1()
        self.window.show_view(char_sel)

# Where player 1 chooses their character
class CharSel1(arcade.View):
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
        arcade.draw_text("Click to advance to Character Selection for Player 2.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150, arcade.color.GRAY, font_size=20, anchor_x="center")

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
        char_sel = CharSel2()
        self.window.show_view(char_sel)

# Where player 2 chooses their character
class CharSel2(arcade.View):
    def __init__(self):
        super().__init__()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        # Loads background image with all character options
        self.background = arcade.load_texture("background2.jpg")

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
        global PLAYER_CHARACTER1

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
        self.time_taken = 0

        # default player image if none selected
        self.player_sprite = Player("../images/monkey.png", SPRITE_SCALING)
        # set up sprites for collision
        self.player_list = arcade.SpriteList()

        self.player_sprite1 = Player("../images/hippo.png", SPRITE_SCALING)
        # set up sprites for collision
        self.player_list1 = arcade.SpriteList()

        self.coin_list = arcade.SpriteList()
        self.badcoin_list = arcade.SpriteList()
        self.wall_list = None

        self.physics_engine = None

        # Chooses corresponding sprite to selection made in Character Selection screen
        if PLAYER_CHARACTER == 1:
            self.player_sprite = arcade.Sprite("../images/character_femaleAdventurer_attack1.png", SPRITE_SCALING)
        elif PLAYER_CHARACTER == 2:
            self.player_sprite = arcade.Sprite("../images/gingerBread_NE.png", SPRITE_SCALING)
        elif PLAYER_CHARACTER == 3:
            self.player_sprite = arcade.Sprite("../images/monkey.png", SPRITE_SCALING)
        elif PLAYER_CHARACTER == 4:
            self.player_sprite = arcade.Sprite("../images/character_maleAdventurer_behindBack.png", SPRITE_SCALING)

        # Chooses corresponding sprite to selection made in Character Selection screen
        if PLAYER_CHARACTER1 == 1:
            self.player_sprite1 = arcade.Sprite("../images/panda.png", SPRITE_SCALING)
        elif PLAYER_CHARACTER1 == 2:
            self.player_sprite1 = arcade.Sprite("../images/hippo.png", SPRITE_SCALING)
        elif PLAYER_CHARACTER1 == 3:
            self.player_sprite1 = arcade.Sprite("../images/frog.png", SPRITE_SCALING)
        elif PLAYER_CHARACTER1 == 4:
            self.player_sprite1 = arcade.Sprite("../images/giraffe.png", SPRITE_SCALING)

        # Set up the player
        self.score = 0
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(5):

            # Create the coin instance
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING / 3)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(5):

            # Create the coin instance
            badcoin = arcade.Sprite("../images/bumper.png", SPRITE_SCALING / 3)

            # Position the coin
            badcoin.center_x = random.randrange(SCREEN_WIDTH)
            badcoin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.badcoin_list.append(badcoin)

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite.center_x = 700
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 100
        self.player_list1.append(self.player_sprite1)

        # Bottom boundary
        for x in range(0, 850, 50):
            wall = arcade.Sprite("../images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 20
            self.wall_list.append(wall)

        # Top boundary
        for x in range(0, 850, 50):
            wall = arcade.Sprite("../images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 580
            self.wall_list.append(wall)

        # Left boundary
        for y in range(0, 610, 30):
            wall = arcade.Sprite("../images/grass.png", SPRITE_SCALING1)
            wall.center_x = 20
            wall.center_y = y
            self.wall_list.append(wall)
        # Right boundary
        for y in range(0, 610, 30):
            wall = arcade.Sprite("../images/grass.png", SPRITE_SCALING1)
            wall.center_x = 780
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        # Draw all the sprites.
        self.player_list.draw()
        self.coin_list.draw()
        self.badcoin_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 30, arcade.color.WHITE, 14)
        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        self.time_taken += delta_time

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.badcoin_list.update()
        self.player_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        hit_list2 = arcade.check_for_collision_with_list(self.player_sprite, self.badcoin_list)

        # Loop through each colliding sprite, remove it, and add to the
        # score.
        for coin in hit_list:
            coin.kill()
            self.score += 1
            self.window.total_score += 1

        for badcoin in hit_list2:
            badcoin.kill()
            self.score -= 1
            self.window.total_score -= 1

        # If we've collected all the games, then move to a "GAME_OVER"
        # state.
        if len(self.coin_list) == 0:
            game_over_view = GameOverWinView()
            game_over_view.time_taken = self.time_taken
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
        game_view = CharSel1()
        self.window.show_view(game_view)

class GameOverLoseView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        arcade.draw_text("Game Over!", 400, 500, arcade.color.BLACK, font_size=40, anchor_x="center")
        arcade.draw_text("Please try again.", 400, 300, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Click to replay.", 200, 200, arcade.color.BLACK, font_size=20, anchor_x="center")

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