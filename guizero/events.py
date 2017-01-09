from enum import Enum


class KeyEvents(Enum):
    """ Keyboard events by Enum used to bind a function to control action """
    KEY_UP = "<KeyRelease>"
    KEY_PRESS = "<KeyPress>"
    FOCUS_IN = "<FocusIn>"
    FOCUS_OUT = "<FocusOut>"


class MouseEvents(Enum):
    """ Mouse events by Enum used to bind a function to control action """
    MOUSE_PRESS_LEFT_BUTTON = "<Button-1>"
    MOUSE_PRESS_MIDDLE_BUTTON = "<Button-2>"
    MOUSE_PRESS_RIGHT_BUTTON = "<Button-3>"
    MOUSE_MOVE_HOLD_LEFT_BUTTON = "<B1-Motion>"
    MOUSE_MOVE_HOLD_MIDDLE_BUTTON = "<B2-Motion>"
    MOUSE_MOVE_HOLD_RIGHT_BUTTON = "<B3-Motion>"
    MOUSE_RELEASE_LEFT_BUTTON = "<ButtonRelease-1>"
    MOUSE_RELEASE_MIDDLE_BUTTON = "<ButtonRelease-2>"
    MOUSE_RELEASE_RIGHT_BUTTON = "<ButtonRelease-3>"
    MOUSE_ENTER = "<Enter>"
    MOUSE_LEAVE = "<Leave>"
    MOUSE_WHEEL = "<MouseWheel>"

    def __value__(self):
        return "X"