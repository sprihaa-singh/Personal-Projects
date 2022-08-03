import arcade
import random
import os

PLAYER_CHARACTER = 0
SPRITE_SCALING = 0.5

SPRITE_SCALING_COIN = 0.04
SPRITE_SCALING_BUMPER = 0.04
SPRITE_SCALING1 = 0.75
COIN_COUNT = 40
BUMPER_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Que Heist"


# Code for Game
class Maze(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()
        self.time_taken = 0

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.badcoin_list = arcade.SpriteList()
        self.wall_list = None

        self.physics_engine = None


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

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = Player("images/monkey.png", SPRITE_SCALING)
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite.center_x = 700
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

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

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)


    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def main():
    start_view = Maze(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()