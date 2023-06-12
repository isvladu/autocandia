"""
Contains static screen coordinates for the bot use
Screen coords are for 1920x1080 screens
(x, y, x+w, y+h) for Vec4 locations, (x, y) for Vec2 locations
"""

from vec4 import Vec4, GameWindow
from vec2 import Vec2

CLAIM_BUTTON_POS: Vec2 = Vec2(960, 900)

PICKUP_BUTTON_POS: Vec2 = Vec2(680, 860)

DEFAULT_LOC: Vec2 = Vec2(200, 200)

PORTAL_LOC: Vec4 = Vec4(GameWindow(430, 210, 530, 380))