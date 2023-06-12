"""
Contains the helper functions of the game.
"""

import ocr
import similarity
from PIL import ImageGrab
import input_functions
import screen_coords

def default_pos() -> None:
    """Moves the mouse to the default position"""
    input_functions.left_click(screen_coords.DEFAULT_LOC)
    
def check_alive() -> bool:
    """Checks if the bot run operation is still running"""
    return True

def get_portal_coords(mode: str) -> tuple | None:
    """Checks if the dungeon has ended and returns the coordinates if it does"""
    screen_capture = ImageGrab.grab(bbox=screen_coords.PORTAL_LOC)
    portal_data = ocr.get_text_from_image(screen_capture, ocr.DEFAULT_PSM)
    length = len(portal_data['level'])
    
    if length == 0:
        return None
    
    for idx in range(length):
        if similarity.similar(portal_data['text'][idx], mode) > 0.9:
            return (portal_data['left'][idx], portal_data['top'][idx], portal_data['width'][idx], portal_data['height'][idx])
        
    return None