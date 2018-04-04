from . import utilities as utils


class EventData():
    
    def __init__(self, widget, tk_event):
        """
        The EventData class represents a single event and is passed back to the callback
        """
        self._widget = widget
        self._tk_event = tk_event

    @property
    def widget(self):
        return self._widget

    @property
    def tk_event(self):
        return self._tk_event

    @property
    def key(self):
        return self._tk_event.char

    @property
    def x(self):
        return self._tk_event.x

    @property
    def y(self):
        return self._tk_event.y

    @property
    def display_x(self):
        return self._tk_event.x_root

    @property
    def display_y(self):
        return self._tk_event.y_root


class EventCallback():

    def __init__(self, widget, tk_event):
        """
        The EventCallback handles all the callbacks for a single tk event (e.g. <Button-1>) on a widget

        By using the EventCallback structure you can assign multiple callbacks to 1 tk event.
        """
        self._widget = widget
        self._tk_event = tk_event
        self._callbacks = {}

        # bind to the tk event
        self._func_id = self._widget.tk.bind(tk_event, self._event_callback)
        
    def _event_callback(self, tk_event):
        # the tk event has fired, run all the callbacks associated to this event
        for ref in self._callbacks:

            callback = self._callbacks[ref]
            args_expected = utils.no_args_expected(callback)

            if args_expected == 0:
                callback()
            elif args_expected == 1:
                callback(EventData(self._widget, tk_event))
            else:
                utils.error_format("An event callback function must accept either 0 or 1 arguments.\nThe current callback has {} arguments.".format(args_expected))    
        
    def get_callback(self, ref):
        """
        Returns the callback for a ref (reference) 
        """
        if ref in self._callbacks:
            return self._callbacks[ref]
        else:
            return None

    def set_callback(self, ref, callback):
        """
        Sets a callback for a ref (reference), setting to None will remove it
        """
        # if the callback already exists, remove it
        self.remove_callback(ref)

        # add it to the callbacks
        if callback is not None:
            self._callbacks[ref] = callback

    def remove_callback(self, ref):
        """
        Removes a callback for a ref (reference),
        """
        if ref in self._callbacks:
            del self._callbacks[ref]

    @property
    def widget(self):
        return self._widget

    @property
    def tk_event(self):
        return self._tk_event

class EventManager():
    
    def __init__(self, widget):
        """
        The EventManager handles all the events and callbacks for a widget.

        Every event created must be given a reference, this reference
        is how events are managed internally within guizero
        """
        self._widget = widget
        self._refs = {}
        self._event_callbacks = {}

    def get_event(self, ref):
        """
        Returns the event callback for a ref (reference) 
        """
        # is this reference one which has been setup?
        if ref in self._refs:
            return self._refs[ref].get_callback(ref)
        else:
            return None

    def set_event(self, ref, tk_event, callback):
        """
        Sets a callback for this widget against a ref (reference) for a tk_event,
        setting the callback to None will remove it.
        """
        # has an EventCallback been created for this tk event
        if tk_event not in self._event_callbacks:
            self._event_callbacks[tk_event] = EventCallback(self._widget, tk_event)
            
        # assign this ref to this event callback
        self._refs[ref] = self._event_callbacks[tk_event]

        # set up the callback
        self._refs[ref].set_callback(ref, callback)
        
    def remove_event(self, ref):
        """
        Removes an event for a ref (reference),
        """
        # is this reference one which has been setup?
        if ref in self._refs:
            self._refs[ref].remove_callback(ref)
        