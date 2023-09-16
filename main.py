import pyautogui
import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'PATH TO tesseract.exe'
from PIL import Image
import keyboard

def screenshot():
    boxes = {
        0: {"top_left": (0, 72), "bottom_right": (2475, 200)},
        1: {"top_left": (62, 520), "bottom_right": (670, 609)},
        2: {"top_left": (730, 520), "bottom_right": (1340, 606)},
        3: {"top_left": (62, 620), "bottom_right": (670, 705)},
        4: {"top_left": (730, 620), "bottom_right": (1340, 704)},
    }
    result = ""
    for element in boxes:
        coords = boxes[element]
        x1, y1 = coords["top_left"]
        x2, y2 = coords["bottom_right"]

        width = x2 - x1
        height = y2 - y1

        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
         # save_path = 'ENTER PATH '     **this line and below line are only needed for testing - mainly to see what screenshots are being generated**
         # screenshot.save(os.path.join(save_path, 'screenshot.png'))
        screenshot_text = tess.image_to_string(screenshot)
        if not screenshot_text.strip():
            print("No text detected.")
            continue
        if element == 0:
            result += f"Question: {screenshot_text}"
        else:
            result += f"{element}: {screenshot_text}"
    print(result)

keyboard.add_hotkey("ctrl+alt+t", screenshot)
keyboard.wait()
