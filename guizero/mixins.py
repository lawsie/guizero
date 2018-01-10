
class MasterMixin():
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


class ContainerMixin():
    """
    Mixin used by all containers 
    """
    @property
    def layout(self):
        """
        Returns the layout type used by this container.
        """
        return self._layout_manager
