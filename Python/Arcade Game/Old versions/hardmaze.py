import arcade
import os
import random

SPRITE_SCALING = 0.5
SPRITE_SCALING1 = .75

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Walls Example"

MOVEMENT_SPEED = 5


class Maze(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

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
        self.chest_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.chest_sprite = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.chest_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 700
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # set up the chest


        # -- Set up the walls
        # Create a row of box

        # Bottom boundary
        for x in range(0, 850, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 20
            self.wall_list.append(wall)

        # Top boundary
        for x in range(0, 850, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 580
            self.wall_list.append(wall)

        # Left boundary
        for y in range(0, 610, 30):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = 20
            wall.center_y = y
            self.wall_list.append(wall)

        # Right boundary
        for y in range(0, 610, 30):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = 780
            wall.center_y = y
            self.wall_list.append(wall)

         # quad 1

        for x in range (210, 260, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 475
            self.wall_list.append(wall)

        for x in range (80, 100, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        for x in range (336, 386, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 330
            self.wall_list.append(wall)
        for y in range(500, 550, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = 378
            wall.center_y = y
            self.wall_list.append(wall)
        #quad2
        for x in range (480, 680, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        for y in range(420, 520, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = 643
            wall.center_y = y
            self.wall_list.append(wall)

        #quad 3
        for x in range(325, 425, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 150
            self.wall_list.append(wall)

        for x in range(175, 225, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 125
            self.wall_list.append(wall)
        for x in range(175, 275, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = x
            wall.center_y = 275
            self.wall_list.append(wall)
        #quad 4
        for y in range(200, 300, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = 580
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(150, 200, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = 425
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(75, 125, 50):
            wall = arcade.Sprite("../../../Downloads/final project/images/grass.png", SPRITE_SCALING1)
            wall.center_x = 575
            wall.center_y = y
            self.wall_list.append(wall)



        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

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
    """ Main method """
    window = Maze(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()