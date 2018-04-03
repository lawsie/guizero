from . import utilities as utils

class EventCallback():

    def __init__(self, tk, event, callback):
        self._tk = tk
        self._event = event
        self._callback = callback
        self._func_id = self._tk.bind(event, self._event_callback)
        
    def _event_callback(self, event):
        args_expected = utils.no_args_expected(self._callback)
        if args_expected == 0:
            self._callback()
        elif args_expected == 1:
            self._callback(event)
        else:
            utils.error_format("Event callback function must accept either 0 or 1 arguments.\nThe current callback has {} arguments.".format(args_expected))    
    
    def clear(self):
        self._tk.unbind(self._event, self._func_id)

    @property
    def event(self):
        return self._event

    @property
    def callback(self):
        return self._callback


class EventManager():
    
    def __init__(self, tk):
        self._tk = tk
        self._events = {}

    def get_event(self, event):
        # if the event exists, clear it
        if event in self._events:
            return self._events[event].callback
        else:
            return None

    def set_event(self, event, callback):
        # if the event exists, clear it
        if event in self._events:
            self._events[event].clear()

        if callback is not None:
            # create a callback event and add it to the dict
            event_callback = EventCallback(self._tk, event, callback)
            self._events[event] = event_callback
        