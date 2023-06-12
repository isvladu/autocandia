"""
Handles tasks that are related to the game itself
"""

import logging
from time import perf_counter, sleep

import win32gui  # type: ignore

import game_functions
import log
from vec2 import Vec2
from vec4 import Vec4

logger = logging.getLogger(__name__)


class Game:
    """Game class that handles game logic"""

    def __init__(self, mode: str = "Restart") -> None:
        self.found_window = False
        self.time = None
        self.mode = mode

        logger.info("Searching for game window...")
        while not self.found_window:
            logger.info("Did not find window, trying again...")
            win32gui.EnumWindows(self.callback, None)
            sleep(1)

        self.startup()

    def callback(self, hwnd, extra) -> None:
        """Function used to find the game window and get its size"""

        if "Nordicandia" not in win32gui.GetWindowText(hwnd):
            return

        rect = win32gui.GetWindowRect(hwnd)

        x_pos = rect[0]
        y_pos = rect[1]
        width = rect[2] - x_pos
        height = rect[3] - y_pos

        if width < 200 or height < 200:
            return

        logger.info(f"Window {win32gui.GetWindowText(hwnd)} found!")
        logger.info(f"Location: {x_pos}, {y_pos}")
        logger.info(f"Size: {width}x{height}")

        Vec4.setup_screen(x_pos, y_pos, width, height)
        Vec2.setup_screen(x_pos, y_pos, width, height)
        self.found_window = True

    def setup(self) -> None:
        """Sets up the game"""
        game_functions.default_pos()
        self.start_time: float = perf_counter()
        self.game_loop()

    def game_loop(self) -> None:
        """Loop that runs while the game is running and the bot is active"""
        while game_functions.check_alive(): # replace with proper condition
            self.time = perf_counter() - self.start_time
