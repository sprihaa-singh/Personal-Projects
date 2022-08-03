import arcade
import random
import os


SPRITE_SCALING = 0.5

SPRITE_SCALING_COIN = 0.04
SPRITE_SCALING_BUMPER = 0.04
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
        arcade.draw_text("Collect both treasure chests before you can escape the maze.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Don't get caught by the police!",SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 70, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Good coins are +1. ", SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 + 40, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Bad coins are -1. Watch out for them.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 10, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Click to advance to Character Selection.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200, arcade.color.GRAY, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # change GameView to name of Character Selection
        char_sel = CharSel()
        self.window.show_view(char_sel)

#
class CharSel(arcade.View):
    def __init__(self):
        super().__init__()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.background = arcade.load_texture("../background.png")

        self.player_sprite = Player("../images/monkey.png", SPRITE_SCALING)

        self.value = 0

    def on_show(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(400, 300, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    def on_draw(self):
        # arcade.start_render()
        arcade.draw_text("Choose a character below:", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Type 'a'", SCREEN_WIDTH /5 - 40, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Type 'b'", 2*SCREEN_WIDTH / 5-20, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Type 'c'", 3*SCREEN_WIDTH / 5+20, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Type 'd'", 4*SCREEN_WIDTH / 5+40, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150, arcade.color.GRAY, font_size=40, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.value = 1
        elif key == arcade.key.DOWN:
            self.value = 2
        elif key == arcade.key.LEFT:
            self.value = 3
        elif key == arcade.key.RIGHT:
            self.value = 4


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


# change code inside this class to actual maze, etc
class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.time_taken = 0
        # value = int(CharSel().get_return)

        self.player_sprite = Player("../images/monkey.png", SPRITE_SCALING)
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        """
        if value == 1:
            self.player_sprite = arcade.Sprite("images/character_femaleAdventurer_attack1.png", SPRITE_SCALING)
        elif value == 2:
            self.player_sprite = arcade.Sprite("images/gingerBread_NE.png", SPRITE_SCALING)
        elif value == 3:
            self.player_sprite = arcade.Sprite("images/monkey.png", SPRITE_SCALING)
        elif value == 4:
            self.player_sprite = arcade.Sprite("images/character_maleAdventurer_behindBack.png", SPRITE_SCALING)
        """

        # Set up the player
        self.score = 0
        #self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
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

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        # Draw all the sprites.
        self.player_list.draw()
        self.coin_list.draw()

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
        self.player_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the
        # score.
        for coin in hit_list:
            coin.kill()
            self.score += 1
            self.window.total_score += 1

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
        game_view = CharSel()
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
        arcade.draw_text("You have been caught by the police!", 400, 500, arcade.color.BLACK, font_size=40, anchor_x="center")
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