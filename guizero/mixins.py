
class MasterMixin():
    @property
    def master(self):
        """
        Returns the master (or container) of this widget.  
        """
        return self._master

    