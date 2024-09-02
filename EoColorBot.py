import pyautogui
import keyboard
from PIL import ImageGrab
from tkinter import Tk, Button, Label, colorchooser
import json
import os

# Global variables to store the player's center position and target colors
PLAYER_CENTER = None
TARGET_COLORS = [None, None, None, None]  # List to store up to 4 colors
CONFIG_FILE = 'eopyconfig.json'

def load_config():
    global PLAYER_CENTER, TARGET_COLORS
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            PLAYER_CENTER = tuple(config['player_center'])
            TARGET_COLORS = [tuple(color) if color else None for color in config['target_colors']]
            update_color_labels()
            print(f"Loaded config: Player Center: {PLAYER_CENTER}, Target Colors: {TARGET_COLORS}")

def save_config():
    config = {
        'player_center': PLAYER_CENTER,
        'target_colors': TARGET_COLORS
    }
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file)
    print(f"Saved config: Player Center: {PLAYER_CENTER}, Target Colors: {TARGET_COLORS}")

def get_color_position(target_color):
    screenshot = ImageGrab.grab()
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == target_color:
                return x, y
    return None

def move_to_color(color_pos):
    pyautogui.moveTo(color_pos)

def click_color(color_pos):
    pyautogui.click(color_pos)

def set_player_center():
    global PLAYER_CENTER
    print("Click on the player to set the center position.")
    PLAYER_CENTER = pyautogui.position()  # Capture the mouse position when the user clicks
    save_config()

def pick_color(index):
    global TARGET_COLORS
    color_code = colorchooser.askcolor(title=f"Choose target color {index+1}")[0]
    if color_code:
        TARGET_COLORS[index] = tuple(map(int, color_code))
        update_color_labels()
        save_config()

def update_color_labels():
    for i, color in enumerate(TARGET_COLORS):
        if color:
            color_labels[i].config(text=f"Target Color {i+1}: {color}")
        else:
            color_labels[i].config(text=f"Target Color {i+1}: Not Set")

def focus_on_target(target_color):
    current_target = None

    while True:
        if current_target is None:
            current_target = get_color_position(target_color)

        if current_target:
            distance_x = abs(current_target[0] - PLAYER_CENTER[0])
            distance_y = abs(current_target[1] - PLAYER_CENTER[1])
            if distance_x > 10 or distance_y > 10:
                move_to_color(current_target)
                current_target = get_color_position(target_color)  # Update target's position while moving
            else:
                click_color(current_target)
                current_target = get_color_position(target_color)  # Re-check if the target is still present
        else:
            break  # Exit loop if the target color is no longer found

def bot_cycle():
    while not keyboard.is_pressed('q'):  # Press 'q' to stop the bot
        for target_color in TARGET_COLORS:
            if target_color:
                focus_on_target(target_color)  # Focus on each target until it's gone

def start_bot():
    if PLAYER_CENTER and any(TARGET_COLORS):
        bot_cycle()
    else:
        print("Please set the player center and at least one target color.")

def create_gui():
    root = Tk()
    root.title("Game Bot Setup")

    global color_labels
    color_labels = [Label(root, text=f"Target Color {i+1}: Not Set") for i in range(4)]
    for label in color_labels:
        label.pack()

    Button(root, text="Set Player Center", command=set_player_center).pack()

    for i in range(4):
        Button(root, text=f"Pick Target Color {i+1}", command=lambda i=i: pick_color(i)).pack()

    Button(root, text="Start Bot", command=start_bot).pack()

    load_config()  # Load configuration on startup

    root.mainloop()

if __name__ == "__main__":
    print("Press 'q' to stop the bot")
    create_gui()
