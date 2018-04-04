from . import utilities as utils


class EventData():
    
    def __init__(self, widget, tk_event):
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

    def __init__(self, widget, event, callback):
        self._widget = widget
        self._event = event
        self._callback = callback
        self._func_id = self._widget.tk.bind(event, self._event_callback)
        
    def _event_callback(self, tk_event):
        args_expected = utils.no_args_expected(self._callback)
        if args_expected == 0:
            self._callback()
        elif args_expected == 1:
            self._callback(EventData(self._widget, tk_event))
        else:
            utils.error_format("An event callback function must accept either 0 or 1 arguments.\nThe current callback has {} arguments.".format(args_expected))    
    
    def clear(self):
        self._widget.tk.unbind(self._event, self._func_id)

    @property
    def event(self):
        return self._event

    @property
    def callback(self):
        return self._callback


class EventManager():
    
    def __init__(self, widget):
        self._widget = widget
        self._events = {}

    def get_event(self, event):
        if event in self._events:
            return self._events[event].callback
        else:
            return None

    def set_event(self, event, callback):
        # if the event exists, clear it
        self.clear_event(event)
        
        if callback is not None:
            # create a callback event and add it to the dict
            self._events[event] = EventCallback(self._widget, event, callback)
        
    def clear_event(self, event):
        if event in self._events:
            self._events[event].clear()
            del self._events[event]