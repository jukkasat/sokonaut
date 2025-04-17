# Sokonaut Game

Sokonaut is a puzzle game where the player navigates through levels, solving challenges to progress. The game features a variety of mechanics, including scoring, level unlocking, and more.

## Features

- **GameState**: Manages the game's state, levels, and logic.
- **Renderer**: Handles graphical rendering.
- **InputHandler**: Processes user input.
- **Main Game Class**: The core of the game.
- **Maps**: Handles level data and map-related logic.
- **HighScores**: Manages scoring and high score persistence.

### Planned Improvements (WIP)
- Level completion screens (e.g., "Level Won", "Game Won").
- Scoring system with high scores and persistent storage.
- Mouse input support.
- Unlockable levels as the player progresses.
- Android port.
- Credits screen with tips.

## Folder Structure

```
sokonaut/
├── src/
│   ├── sokonaut.py
│   ├── main.py
│   ├── game_state.py
│   ├── renderer.py
│   ├── input_handler.py
│   ├── maps.py
│   ├── high_scores.py
│   └── img/
├── README.md
├── main.py
└── requirements.txt
```

## How to Run

1. **Install Dependencies**:
   Ensure you have Python installed. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Game**:
   Navigate to the `src` directory and execute the main game file:
   ```bash
   python main.py
   ```

3. **Enjoy the Game**:
   Use the keyboard (or mouse, if implemented) to play the game.

## Contributing

Feel free to contribute to the project by submitting pull requests or reporting issues. Planned improvements are listed above, but additional ideas are welcome!