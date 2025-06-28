import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Ping Pong "

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
BALL_RADIUS = 10

class SimplePingPong(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_BLUE)

        self.left_paddle_x = 30
        self.left_paddle_y = SCREEN_HEIGHT // 2

        self.right_paddle_x = SCREEN_WIDTH - 30
        self.right_paddle_y = SCREEN_HEIGHT // 2

        self.ball_x = SCREEN_WIDTH // 2
        self.ball_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rect_filled(self.left_paddle_x, self.left_paddle_y,PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)

        arcade.draw_rect_filled(self.right_paddle_x, self.right_paddle_y,PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)

        arcade.draw_circle_filled(self.ball_x, self.ball_y, BALL_RADIUS, arcade.color.WHITE)

        arcade.draw_line(SCREEN_WIDTH // 2, 0, SCREEN_WIDTH // 2,SCREEN_HEIGHT, arcade.color.WHITE, 2)

        arcade.finish_render()

if __name__ == "__main__":
    game = SimplePingPong()
    arcade.run()
