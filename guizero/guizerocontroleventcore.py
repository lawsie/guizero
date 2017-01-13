
class GuiZeroControlEventCore:
    # Bind to Events

    def on_mouse_press_left_button(self, func, add=""):
        """ Delegates the action when the left mouse button (or button 1) is pressed  """
        self.bind(MouseEvents.MOUSE_PRESS_LEFT_BUTTON, func, add)

    def on_mouse_press_middle_button(self, func, add=""):
        """ Delegates the action when the middle mouse button (or button 2) is pressed  """
        self.bind(MouseEvents.MOUSE_PRESS_MIDDLE_BUTTON, func, add)

    def on_mouse_press_right_button(self, func, add=""):
        """ Delegates the action when the left mouse button (or button 3) is pressed  """
        self.bind(MouseEvents.MOUSE_PRESS_RIGHT_BUTTON, func, add)

    def on_mouse_move_hold_left_button(self, func, add=""):
        """ Delegates the action when the mouse is moved with the left mouse button (or button 1) held down  """
        self.bind(MouseEvents.MOUSE_MOVE_HOLD_LEFT_BUTTON, func, add)

    def on_mouse_move_hold_middle_button(self, func, add=""):
        """ Delegates the action when the mouse is moved with the middle mouse button (or button 2) held down  """
        self.bind(MouseEvents.MOUSE_MOVE_HOLD_MIDDLE_BUTTON, func, add)

    def on_mouse_move_hold_right_button(self, func, add=""):
        """ Delegates the action when the mouse is moved with the right mouse button (or button 3) held down  """
        self.bind(MouseEvents.MOUSE_MOVE_HOLD_RIGHT_BUTTON, func, add)

    def on_mouse_release_left_button(self, func, add=""):
        """ Delegates the action when the mouse left mouse button (or button 1) is released """
        self.bind(MouseEvents.MOUSE_RELEASE_LEFT_BUTTON, func, add)

    def on_mouse_release_middle_button(self, func, add=""):
        """ Delegates the action when the mouse middle mouse button (or button 2) is released """
        self.bind(MouseEvents.MOUSE_RELEASE_MIDDLE_BUTTON, func, add)

    def on_mouse_release_right_button(self, func, add=""):
        """ Delegates the action when the mouse right mouse button (or button 3) is released """
        self.bind(MouseEvents.MOUSE_RELEASE_RIGHT_BUTTON, func, add)

    def on_mouse_enter(self, func, add=""):
        """ Delegates the action when the mouse passes over the control """
        self.bind(MouseEvents.MOUSE_ENTER, func, add)

    def on_mouse_leave(self, func, add=""):
        """ Delegates the action when the mouse has passed over the control """
        self.bind(MouseEvents.MOUSE_LEAVE, func, add)

    def on_key_up(self, func, add=""):
        """ Delegates the action when a key is released (after the letter has appeared) """
        self.bind(KeyEvents.KEY_UP, func, add)

    def on_key_down(self, func, add=""):
        """ Delegates the action when a key is pressed (before the letter has appeared) """
        self.bind(KeyEvents.KEY_PRESS, func, add)

    def on_focus_in(self, func, add=""):
        """ Delegates the action when the control receives focus """
        self.bind(KeyEvents.FOCUS_IN, func, add)

    def on_focus_out(self, func, add=""):
        """ Delegates the action when the control no longer has focus """
        self.bind(KeyEvents.FOCUS_OUT, func, add)

class KeyEvents:
    """ Keyboard events to bind a function to control action """
    KEY_UP = "<KeyRelease>"
    KEY_PRESS = "<KeyPress>"
    FOCUS_IN = "<FocusIn>"
    FOCUS_OUT = "<FocusOut>"


class MouseEvents:
    """ Mouse events to bind a function to control action """
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