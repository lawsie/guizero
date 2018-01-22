
class EventMixin():
    """
    Mixin used by all components that receive events
    """

    @property
    def when_mouse_moved(self):
        return self._motion_command

    @property
    def when_mouse_dragged(self):
        return self._drag_command

    @property
    def when_mouse_clicked(self):
        return self._click_command

    @property
    def when_key_pressed(self):
        return self._key_command
    
    @when_mouse_moved.setter
    def when_mouse_moved(self,command):
        self._motion_command = command
        self.tk.bind('<Motion>',lambda event: command(event.x,event.y))

    @when_mouse_dragged.setter
    def when_mouse_dragged(self,command):
        self._drag_command = command
        self.tk.bind('<B1-Motion>',lambda event: command(event.x,event.y))

    @when_mouse_clicked.setter
    def when_mouse_clicked(self,command):
        self._click_command = command
        self.tk.bind('<Button-1>',lambda event: command(event.x,event.y))

    @when_key_pressed.setter
    def when_key_pressed(self,command):
        self._key_command = command
        self.tk.bind('<Key>',lambda event: command(event.keysym))

class MasterMixin(EventMixin):
    """
    Mixin used by all components which have a master
    """
    @property
    def master(self):
        """
        Returns the master (or container) of this widget.  
        """
        return self._master


class WidgetMixin(MasterMixin):
    """
    Mixin used by all widgets
    """       
    
    @property
    def grid(self):
        """
        Returns `[x,y]` coordinates of this widget.
        """
        return self._grid

    @property
    def align(self):
        """
        Returns the alignment of this widget within its grid location.
        """
        return self._align

class ContainerMixin(EventMixin):
    """
    Mixin used by all containers 
    """
    @property
    def layout(self):
        """
        Returns the layout type used by this container.
        """
        return self._layout_manager

