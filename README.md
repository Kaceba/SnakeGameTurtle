# SnakeGameTurtle

A classic Snake game implementation in Python using the Turtle graphics library.

## Features

- Classic snake gameplay
- Score tracking
- Collision detection (walls and self)
- Smooth movement with keyboard controls
- Game over screen

## Requirements

- Python 3.x
- turtle (built-in with Python)

## Installation

1. Clone or download the game files
2. Ensure you have the following files in the same directory:
   - `main.py` (main game file)
   - `snake.py` (Snake class)
   - `food.py` (Food class)
   - `scoreboard.py` (Scoreboard class)

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. Use arrow keys to control the snake:
   - ↑ Up Arrow: Move up
   - ↓ Down Arrow: Move down
   - ← Left Arrow: Move left
   - → Right Arrow: Move right

3. Eat the food to grow and increase your score
4. Avoid hitting the walls or your own tail
5. Click anywhere to exit after game over

## Game Rules

- The snake moves continuously in the current direction
- Eating food makes the snake longer and increases the score
- Game ends when the snake hits a wall or itself
- The play area is 600x600 pixels with boundaries at ±280 pixels

## File Structure

- `main.py` - Main game loop and event handling
- `snake.py` - Snake class with movement and growth logic
- `food.py` - Food class for random food placement
- `scoreboard.py` - Score display and game over screen

## Game Settings

- Window size: 600x600 pixels
- Background: Black
- Game speed: 0.1 second delay between moves
- Food detection distance: 20 pixels
- Self-collision detection distance: 10 pixels

## Customization

You can modify the game by adjusting:
- Window size in `screen.setup()`
- Game speed by changing `time.sleep()` value
- Colors in individual class files
- Collision detection distances

Enjoy playing!
