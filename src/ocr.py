"""
Contains all methods required to translate an image into a data string
"""

from typing import Any

import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab, Image

import settings

pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_PATH

ALPHABET_WHITELIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ROUND_WHITELIST = "0123456789-"


def image_grayscale(image: ImageGrab.Image) -> cv2.Mat:
    """Converts image to grayscale"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def image_thresholding(image: ImageGrab.Image) -> cv2.Mat:
    """Applies thresholding to image"""
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


def image_array(image: ImageGrab.Image) -> Any:
    """Turns image into an array"""
    image = np.array(image)
    image = image[..., :3]

    return image


def image_resize(image: ImageGrab.Image, scale: int) -> Any:
    """Resizes the image using the scale parameter"""
    (width, height) = (image.width * scale, image.height * scale)

    return image.resize((width, height))


def get_text(screenxy: tuple, scale: int, psm: int, whitelist: str = "") -> str:
    """Returns text from screen coordinates"""
    screenshot = ImageGrab.grab(bbox=screenxy)
    resize = image_resize(screenshot, scale)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)

    return pytesseract.image_to_string(
        thresholding, config=f"--psm {psm} -c tessedit_char_whitelist={whitelist}"
    ).strip()


def get_text_from_image(image: ImageGrab.Image, psm: int, whitelist: str = "") -> str:
    """Takes an image and returns the text"""
    resize = image_resize(image, 3)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    
    cv2.namedWindow("Thresholding", cv2.WINDOW_NORMAL)
    cv2.imshow("Thresholding", thresholding)
    cv2.resizeWindow("Thresholding", 800, 600)

    cv2.waitKey(0)

    return pytesseract.image_to_string(
        thresholding, config=f"--psm {psm} -c tessedit_char_whitelist={whitelist}"
    ).strip()

def get_orientation(image: ImageGrab.Image, whitelist: str = "") -> str:
    resize = image_resize(image, 3)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    
    cv2.imshow("Thresholding", thresholding)
    cv2.waitKey(0)
    
    return pytesseract.image_to_osd(
        thresholding, config=f"-c tessedit_char_whitelist={whitelist}", output_type=pytesseract.Output.DICT
    )

im = Image.open("images/portal_test_ss.png")
# im = im.crop((750, 250, 950, 400))
im_copy = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
rotation_matrix = cv2.getRotationMatrix2D((im_copy.shape[1]/2, im_copy.shape[0]/2), 22, 1)
im_copy = cv2.warpAffine(im_copy, rotation_matrix, (im_copy.shape[1], im_copy.shape[0]))
im_copy = cv2.cvtColor(im_copy, cv2.COLOR_BGR2RGB)
im_copy = Image.fromarray(im_copy)
#print(get_orientation(im))
print(get_text_from_image(im_copy, 11))
#print(get_text_from_image(im, 3, ALPHABET_WHITELIST))