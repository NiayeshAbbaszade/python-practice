import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Ping Pong "

class SimplePingPong(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.YELLOW)
        self.ball_x = 400
        self.ball_y= 200
        
    def on_draw (self):
        arcade.draw_line(400,400,400,0,arcade.color.SKY_BLUE,5)
        arcade.draw_circle_filled(self.ball_x,self.ball_y,20,arcade.color.BLUE_GREEN)
    def on_update(self, delta_time):
        self.ball_x+=2

game=SimplePingPong()
arcade.run()     