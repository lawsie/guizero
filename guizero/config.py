# holds details about the configuration guizero is using
import sys

class SystemConfig():

    def __init__(self):
        self._platform = sys.platform
        if self._platform.startswith("linux"):
            self._platform = "linux"
        
        self._supported_image_types = ["GIF", "PNG"]
        if self._platform == "darwin":
            #MacOS only supports GIF
            self._supported_image_types = ["GIF"]

    @property
    def supported_image_types(self):
        return self._supported_image_types

    @property
    def platform(self):
        return self._platform

system_config = SystemConfig()