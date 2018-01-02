
class MasterMixin():
    @property
    def master(self):
        """
        Returns the master (or container) of this widget.  
        """
        return self._master


class ContainerMixin():
    @property
    def layout(self):
        """
        Returns the layout type used by this container.
        """
        return self._layout_manager
