# holds details about the configuration guizero is using
import sys

class SystemConfig():

    def __init__(self):
        try:
            import PIL
            self._PIL_available = True
        except ImportError:
            self._PIL_available = False

        self._platform = sys.platform
        if self._platform.startswith("linux"):
            self._platform = "linux"

        if self._PIL_available:
            self._supported_image_types = ["GIF", "PNG", "JPG"]
        else:
            self._supported_image_types = ["GIF", "PNG"]
            if self._platform == "darwin":
                #MacOS only supports GIF with PIL
                self._supported_image_types = ["GIF"]

    @property
    def supported_image_types(self):
        return self._supported_image_types

    @property
    def platform(self):
        return self._platform

    @property
    def PIL_available(self):
        return self._PIL_available


system_config = SystemConfig()