from . import utilities as utils


class EventData():

    def __init__(self, widget, tk_event):
        """
        The EventData class represents a single event and is passed back to
        the callback
        """
        self._widget = widget
        self._tk_event = tk_event

    @property
    def widget(self):
        """
        The guizero widget which raised the event
        """
        return self._widget

    @property
    def tk_event(self):
        """
        The tkinter event which was returned by the event
        """
        return self._tk_event

    @property
    def key(self):
        """
        The key which was pressed and generated the event.
        """
        return self._tk_event.char

    @property
    def x(self):
        """
        The x position of the mouse relative to the upper left hand corner of
        the widget when the event occurred.
        """
        return self._tk_event.x

    @property
    def y(self):
        """
        The y position of the mouse relative to the upper left hand corner of
        the widget when the event occurred.
        """
        return self._tk_event.y

    @property
    def display_x(self):
        """
        The x position of the mouse relative to the upper left hand corner of
        the display when the event occurred.
        """
        return self._tk_event.x_root

    @property
    def display_y(self):
        """
        The y position of the mouse relative to the upper left hand corner of
        the display when the event occurred.
        """
        return self._tk_event.y_root


class EventCallback():

    def __init__(self, widget, tks, tk_event):
        """
        The EventCallback handles all the callbacks for a single tk event
        (e.g. <Button-1>) on a guizero widget.

        By using the EventCallback structure you can assign multiple callbacks
        to 1 tk event across multiple tk widgets.
        """
        self._widget = widget
        self._tks = tks
        self._tk_event = tk_event
        self._callbacks = {}
        self._func_ids = []

        # bind to the tk event
        for tk in self._tks:
            func_id = tk.bind(tk_event, self._event_callback)
            self._func_ids.append(func_id)

    def _event_callback(self, tk_event):
        # the tk event has fired, run all the callbacks associated to this event
        for ref in self._callbacks.copy():
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

    def rebind(self, tks):
        """
        Rebinds the tk event, only used if a widget has been destroyed
        and recreated.
        """
        self._tks = tks
        for tk in self._tks:
            tk.unbind_all(self._tk_event)
            func_id = tk.bind(self._tk_event, self._event_callback)
            self._func_ids.append(func_id)

    @property
    def widget(self):
        return self._widget

    @property
    def tk_event(self):
        return self._tk_event


class EventManager():

    def __init__(self, widget, *tks):
        """
        The EventManager handles all the events and callbacks for a guizero
        widget.

        Every event created must be given a reference, this reference
        is how events are managed internally within guizero.

        A guizero widget can contain many tk widgets, so all the tk objects
        for this guizero widget need to passed.
        """
        self._widget = widget
        self._tks = tks
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
        Sets a callback for this widget against a ref (reference) for a
        tk_event, setting the callback to None will remove it.
        """
        # has an EventCallback been created for this tk event
        if tk_event not in self._event_callbacks:
            self._event_callbacks[tk_event] = EventCallback(self._widget, self._tks, tk_event)

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

    def rebind_events(self, *tks):
        """
        Rebinds all the tk events, only used if a tk widget has been destroyed
        and recreated.
        """
        for ref in self._refs:
            self._refs[ref].rebind(tks)
