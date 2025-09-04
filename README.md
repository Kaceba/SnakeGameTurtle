# SnakeGameTurtle

A purposefully over engineerd Snake game implementation in Python using the Turtle graphics library with cool features and improved gameplay experience.

<img width="748" height="787" alt="image" src="https://github.com/user-attachments/assets/2db5b20a-125b-48cc-b607-d47c61d581e1" />

## Features

### Core Gameplay
- Classic snake gameplay with smooth movement
- Real-time score tracking
- Comprehensive collision detection (walls and self)
- Game over screen with restart option

### Enhanced Features
- **Pause/Resume**: Pause the game anytime during play
- **Instant Restart**: Restart without closing the game window
- **Dynamic Speed**: Game speed increases as your score grows
- **Reverse Direction Prevention**: Can't move directly backwards into your body
- **Improved Collision Detection**: More accurate tail collision detection
- **Error Handling**: Robust error handling prevents crashes
- **User-Friendly Interface**: Clear instructions and status updates

## Requirements

- Python 3.x
- turtle (built-in with Python)

## Installation

1. Clone or download the game files
2. Ensure you have the following files in the same directory:
   - `main.py` (main game file with SnakeGame class)
   - `snake.py` (Snake class)
   - `food.py` (Food class)
   - `scoreboard.py` (Scoreboard class)

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. **Game Controls:**
   - **↑ Up Arrow**: Move up
   - **↓ Down Arrow**: Move down  
   - **← Left Arrow**: Move left
   - **→ Right Arrow**: Move right
   - **SPACE**: Pause/Resume game
   - **R**: Restart game
   - **Click screen**: Exit game

3. **Gameplay:**
   - Eat the blue food to grow and increase your score
   - Avoid hitting the walls or your own tail
   - Game speed increases as your score gets higher
   - Use pause feature to take breaks during long games

## Game Rules

- The snake moves continuously in the current direction
- Eating food makes the snake longer and increases the score by 1
- Game ends when the snake hits a wall or itself
- You cannot move directly backwards into your own body
- The play area is 600x600 pixels with boundaries at ±280 pixels
- Game speed starts at 0.1 seconds per move and decreases as score increases

## File Structure

### Core Files
- `main.py` - Main SnakeGame class with game loop, controls, and enhanced features
- `snake.py` - Snake class with movement, growth, and direction logic
- `food.py` - Food class for random food placement
- `scoreboard.py` - Score display, game over screen, and reset functionality

### Class Architecture
- **SnakeGame**: Main game controller handling screen setup, game loop, collision detection, and user input
- **Snake**: Manages snake segments, movement, growth, and direction changes
- **Food**: Handles food positioning and refresh mechanics  
- **Scoreboard**: Manages score display, updates, and reset functionality

## Game Settings & Constants

### Display Settings
- Window size: 600x600 pixels
- Background: Black
- Snake color: White
- Food color: Blue
- Score font: Courier, 24pt

### Gameplay Settings
- Base game speed: 0.1 seconds between moves
- Minimum game speed: 0.05 seconds (maximum speed)
- Speed increase rate: 0.003 seconds per point scored
- Food collision distance: 20 pixels
- Self-collision distance: 10 pixels
- Wall boundaries: ±280 pixels

## Customization

You can easily modify the game by adjusting constants in `main.py`:

```python
# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Game speed settings
BASE_GAME_SPEED = 0.1
MIN_GAME_SPEED = 0.05
SPEED_INCREASE_RATE = 0.003

# Collision detection
FOOD_COLLISION_DISTANCE = 20
TAIL_COLLISION_DISTANCE = 10
```

### Other Customizations
- Colors can be modified in individual class files
- Snake starting length in `snake.py` STARTING_POSITIONS
- Food appearance in `food.py` shape and color settings
- Score display format in `scoreboard.py`

## Technical Improvements

### Code Quality
- Object-oriented design with proper separation of concerns
- Constants instead of magic numbers for easy configuration
- Comprehensive error handling and logging
- Clean, documented code structure

### Bug Fixes
- Fixed tail collision detection logic
- Improved game state management
- Better memory management for game restarts

### Performance
- Optimized collision detection algorithms
- Efficient game loop with proper frame timing
- Dynamic speed adjustment system

## Troubleshooting

**Game not starting?**
- Ensure all four Python files are in the same directory
- Check that Python 3.x is installed
- Verify turtle graphics is available (usually built-in)

**Controls not working?**
- Click on the game window to ensure it has focus
- Try pressing keys while the game window is active

**Game running too fast/slow?**
- Modify `BASE_GAME_SPEED` constant in main.py
- Adjust `SPEED_INCREASE_RATE` to change speed progression
