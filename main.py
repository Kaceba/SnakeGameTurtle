import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WALL_BOUNDARY = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 2 - 20  # Dynamic boundary based on screen size
FOOD_COLLISION_DISTANCE = 20
TAIL_COLLISION_DISTANCE = 10
BASE_GAME_SPEED = 0.1
MIN_GAME_SPEED = 0.05
SPEED_INCREASE_RATE = 0.003


class SnakeGame:
    def __init__(self):
        self.screen = None
        self.setup_screen()
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.game_is_on = True
        self.paused = False
        self.setup_controls()

    def setup_screen(self):
        """Initialize and configure the game screen."""
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.getcanvas().winfo_toplevel().resizable(False, False)
        self.screen.tracer(0)

    def setup_controls(self):
        """Set up keyboard controls for the game."""
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.toggle_pause, "space")
        self.screen.onkey(self.restart_game, "r")

    def toggle_pause(self):
        """Toggle game pause state."""
        self.paused = not self.paused
        if self.paused:
            self.screen.title("Snake Game - PAUSED (Press SPACE to resume)")
        else:
            self.screen.title("Snake Game")

    def restart_game(self):
        """Restart the game with fresh state."""
        try:
            self.snake = Snake()
            self.food = Food()
            self.scoreboard.reset()
            self.game_is_on = True
            self.paused = False
            self.screen.title("Snake Game")
        except Exception as e:
            print(f"Error restarting game: {e}")

    def get_game_speed(self):
        """Calculate current game speed based on score."""
        speed_increase = self.scoreboard.score * SPEED_INCREASE_RATE
        return max(MIN_GAME_SPEED, BASE_GAME_SPEED - speed_increase)

    def check_food_collision(self):
        """Check if snake has eaten food."""
        if self.snake.head.distance(self.food) < FOOD_COLLISION_DISTANCE:
            try:
                self.food.refresh()
                self.snake.extend()
                self.scoreboard.increase_score()
                return True
            except Exception as e:
                print(f"Error handling food collision: {e}")
        return False

    def check_wall_collision(self):
        """Check if snake has hit the walls."""
        x, y = self.snake.head.xcor(), self.snake.head.ycor()
        return (x > WALL_BOUNDARY or x < -WALL_BOUNDARY or
                y > WALL_BOUNDARY or y < -WALL_BOUNDARY)

    def check_tail_collision(self):
        """Check if snake has collided with its own tail."""
        # Skip the head (first segment) when checking collisions
        for segment in self.snake.segments[1:]:
            if self.snake.head.distance(segment) < TAIL_COLLISION_DISTANCE:
                return True
        return False

    def game_over(self):
        """Handle game over state."""
        self.game_is_on = False
        self.scoreboard.game_over()
        self.screen.title("Snake Game - GAME OVER! Press 'R' to restart")

    def update_game(self):
        """Update game state for one frame."""
        self.screen.update()

        if not self.paused:
            try:
                self.snake.move()

                self.check_food_collision()

                if self.check_wall_collision():
                    self.game_over()
                    return

                if self.check_tail_collision():
                    self.game_over()
                    return

            except Exception as e:
                print(f"Error updating game: {e}")
                self.game_over()

        # Use dynamic speed based on score
        time.sleep(self.get_game_speed())

    def run(self):
        """Main game loop."""
        print("Snake Game Controls:")
        print("Arrow Keys - Move snake")
        print("SPACE - Pause/Resume")
        print("R - Restart game")
        print("Click screen to exit")

        while self.game_is_on:
            self.update_game()

        # Keep screen open for restart option
        while True:
            try:
                self.screen.update()
                time.sleep(0.1)
            except:
                break


def main():
    """Initialize and run the Snake Game."""
    try:
        game = SnakeGame()
        game.run()
        game.screen.exitonclick()
    except Exception as e:
        print(f"Error running game: {e}")


if __name__ == "__main__":
    main()

