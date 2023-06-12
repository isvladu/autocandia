"""
Contains all methods required to translate an image into a data string
"""

import logging
from typing import Any

import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageGrab

import log
import settings

pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_PATH_WINDOWS
logger = logging.getLogger(__name__)

ALPHABET_WHITELIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ROUND_WHITELIST = "0123456789-"
DEFAULT_ANGLE = 22
DEFAULT_PSM = 11


def image_grayscale(image: ImageGrab.Image) -> cv2.Mat:
    """Converts image to grayscale"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def image_thresholding(image: ImageGrab.Image) -> cv2.Mat:
    """Applies thresholding to image"""
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


def image_canny(image: ImageGrab.Image) -> cv2.Mat:
    """Applies canny edge detection to image"""
    return cv2.Canny(image, 100, 200)


def image_array(image: ImageGrab.Image) -> Any:
    """Turns image into an array"""
    image = np.array(image)
    image = image[..., :3]

    return image


def image_resize(image: ImageGrab.Image, scale: int) -> Any:
    """Resizes the image using the scale parameter"""
    (width, height) = (image.width * scale, image.height * scale)

    return image.resize((width, height))


def image_tilt(image: ImageGrab.Image, angle: int) -> Any:
    """Tilts the image to an angle using the angle parameter"""
    tilted_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    rotation_matrix = cv2.getRotationMatrix2D(
        (tilted_image.shape[1] / 2, tilted_image.shape[0] / 2), angle, 1
    )
    tilted_image = cv2.warpAffine(
        tilted_image, rotation_matrix, (tilted_image.shape[1], tilted_image.shape[0])
    )
    tilted_image = cv2.cvtColor(tilted_image, cv2.COLOR_BGR2RGB)
    tilted_image = Image.fromarray(tilted_image)

    return tilted_image


def get_text(screenxy: tuple, scale: int, psm: int, whitelist: str = "") -> dict:
    """Returns text from screen coordinates"""
    screenshot = ImageGrab.grab(bbox=screenxy)
    resize = image_resize(screenshot, scale)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    canny = image_canny(grayscale)

    return pytesseract.image_to_data(
        canny,
        config=f"--psm {psm} -c tessedit_char_whitelist={whitelist}",
        output_type=pytesseract.Output.DICT,
    )


def get_text_from_image(image: ImageGrab.Image, psm: int, whitelist: str = "") -> dict:
    """Takes an image and returns the text"""
    resize = image_resize(image, 3)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    canny = image_canny(grayscale)

    cv2.namedWindow("Thresholding", cv2.WINDOW_NORMAL)
    cv2.imshow("Thresholding", canny)
    cv2.resizeWindow("Thresholding", 800, 600)

    cv2.waitKey(0)

    return pytesseract.image_to_data(
        canny,
        config=f"--psm {psm} -c tessedit_char_whitelist={whitelist}",
        output_type=pytesseract.Output.DICT,
    )


im = Image.open("images/portal_test_ss.png")
# im = im.crop((750, 250, 950, 400))
x = get_text_from_image(image_tilt(im, DEFAULT_ANGLE), DEFAULT_PSM)
for i in range(len(x['level'])):
    if x['text'][i] == "Level":
        logger.info(f"x: {x['left'][i]} y: {x['top'][i]} w: {x['width'][i]} h: {x['height'][i]}")
