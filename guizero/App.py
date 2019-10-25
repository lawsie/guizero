from tkinter import Tk, Toplevel
from .base import BaseWindow
from . import utilities as utils, system_config


class App(BaseWindow):

    _main_app = None

    def __init__(
        self, 
        title="guizero", 
        width=500, 
        height=500, 
        layout="auto", 
        bgcolor=None, 
        bg=None, 
        visible=True):

        """
        Creates an App

        :param string title:
            The text in the title bar of the window, defaults to `guizero`.

        :param int width:
            The width of the App window, defaults to 500.

        :param int height:
            The height of the App window, defaults to 500.

        :param string layout:
            The layout manager style for this window, defaults to `auto`.

        :param string bgcolor:
            DEPRECATED: The background colour for this window, defaults to None. Use bg instead.

        :param color bg:
            The background colour for this window, defaults to None. See https://lawsie.github.io/guizero/colors/

        :param bool visible:
            If the widget should be visible, defaults to `True`.

        """

        description = "[App] object"

        # If this is the first app to be created, create Tk
        if App._main_app is None:
            tk = Tk()
            App._main_app = self
            # apply tk options
            for option_key in system_config.tk_options:
                tk.option_add(option_key, system_config.tk_options[option_key])
        else:
            tk = Toplevel(App._main_app.tk)
            utils.error_format("There should only be 1 guizero App, use Window to create multiple windows.")

        super(App, self).__init__(
            None,
            tk,
            description,
            title,
            width,
            height,
            layout,
            bg,
            visible)

    # METHODS
    # --------------------------------------


    def display(self):
        """
        Display the window.

        :return:
            None.
        """
        self.tk.mainloop()

    def destroy(self):
        """
        Destroy and close the App.

        :return:
            None.

         :note:
            Once destroyed an App can no longer be used.
        """
        # if this is the main_app - set the _main_app class variable to `None`.
        if self == App._main_app:
            App._main_app = None
        self.tk.destroy()
