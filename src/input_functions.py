"""
This module contains functions that are used to simulate input
"""
import random
import pydirectinput


def left_click(coords: tuple) -> None:
    """Left clicks at argument ones coordinates"""
    pydirectinput.moveTo(coords[0], coords[1])
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()


def right_click(coords: tuple) -> None:
    """Right clicks at argument ones coordinates"""
    offset: int = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0], coords[1])
    pydirectinput.mouseDown(button="right")
    pydirectinput.mouseUp(button="right")


def press_space() -> None:
    """Presses spacebar"""
    pydirectinput.press("space")


def press_q() -> None:
    """Presses Q"""
    pydirectinput.press("q")


def press_w() -> None:
    """Presses W"""
    pydirectinput.press("w")


def press_1(coords: tuple, is_aimed: bool) -> None:
    """Presses 1"""
    if is_aimed:
        pydirectinput.moveTo(coords[0], coords[1])
        pydirectinput.press("1")
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    else:
        pydirectinput.press("1")


def press_2(coords: tuple, is_aimed: bool) -> None:
    """Presses 2"""
    if is_aimed:
        pydirectinput.moveTo(coords[0], coords[1])
        pydirectinput.press("2")
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    else:
        pydirectinput.press("2")


def press_3(coords: tuple, is_aimed: bool) -> None:
    """Presses 3"""
    if is_aimed:
        pydirectinput.moveTo(coords[0], coords[1])
        pydirectinput.press("3")
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    else:
        pydirectinput.press("3")


def press_4(coords: tuple, is_aimed: bool) -> None:
    """Presses 4"""
    if is_aimed:
        pydirectinput.moveTo(coords[0], coords[1])
        pydirectinput.press("4")
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    else:
        pydirectinput.press("4")
