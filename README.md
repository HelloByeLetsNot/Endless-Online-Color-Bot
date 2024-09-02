# EOColor Bot


---

# Game Bot

This bot is designed to automate the task of targeting and interacting with specific elements (colors) in a game window. The player is always centered in the game window, and the bot will move towards a target color, staying focused on it until it is completely gone.

## Features

- **Target Focus**: The bot will focus on a single target color until it is no longer present on the screen.
- **Movement and Interaction**: The bot moves towards the target and clicks on it until it disappears.
- **GUI Interface**: Allows the user to easily set up the bot, including setting the player's center position and choosing the target color.
- **Configuration Persistence**: The bot saves the player's center position and target color to a JSON file (`eopyconfig.json`) for easy reloading.

## Requirements

- Python 3.x
- `pyautogui`
- `keyboard`
- `PIL` (Pillow)

You can install the required packages using:

```bash
pip install pyautogui keyboard pillow
```

## Usage

1. **Run the Script**: Start the bot by running the Python script.

2. **Set Player Center**: 
   - Click the "Set Player Center" button in the GUI.
   - Click on the player's character in the game window to set the center position.

3. **Pick Target Color**:
   - Click the "Pick Target Color" button in the GUI.
   - Use the color picker to select the color of the target you want the bot to focus on.

4. **Start the Bot**:
   - Click the "Start Bot" button.
   - The bot will begin moving towards and interacting with the selected target color in the game.

5. **Stop the Bot**:
   - Press `q` on your keyboard at any time to stop the bot.

## Configuration

- The bot automatically saves the player's center position and the target color to a configuration file named `eopyconfig.json`. This file will be loaded the next time you run the script, so you don’t have to reconfigure the bot every time.

## Important Notes

- Ensure the game window remains in the foreground and the player’s position doesn’t change after setting the player center.
- The bot uses screen coordinates to detect and interact with the target color, so any changes to screen resolution or game window size might affect its performance.
- The bot will only work with the specific color selected, so it’s important to choose a color that remains consistent throughout the 
