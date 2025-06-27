import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

class PingPongGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Ping Pong Game")
        arcade.set_background_color(arcade.color.RED)

        self.paddle_left = [50, SCREEN_HEIGHT // 2, 10, 100]  # x, y, width, height
        self.paddle_right = [SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2, 10, 100]

        self.ball = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10]  # x, y, radius

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.paddle_left[0], self.paddle_left[1], self.paddle_left[2], self.paddle_left[3], arcade.color.WHITE)
        arcade.draw_rectangle_filled(self.paddle_right[0], self.paddle_right[1], self.paddle_right[2], self.paddle_right[3], arcade.color.WHITE)
        arcade.draw_circle_filled(self.ball[0], self.ball[1], self.ball[2], arcade.color.WHITE)

        arcade.draw_line(SCREEN_WIDTH // 2, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT, arcade.color.WHITE, 2)

    def update(self, delta_time):
       
        pass

if __name__ == "__main__":
    game = PingPongGame()
    arcade.run()
