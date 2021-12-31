from guizero import App, MenuBar
from threading import Event
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test
    )

def test_legacy_initial_values():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    # Using positional arguments as that is most likely to cause error with
    # it having to detect the legacy system.
    m = MenuBar(
        a,
        ["foo", "bar"],
        [
            [ ["foo1", callback], ["foo2", callback] ],
            [ ["bar1", callback], ["bar2", callback] ]
        ])

    assert m.master == a

    assert not callback_event.is_set()
    assert a.description > ""

    # menu invoke doesnt work...
    # m.tk.invoke(0)
    # assert callback_event.is_set()

    a.destroy()

def test_initial_values():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    # Using positional arguments as that is most likely to cause error with
    # it having to detect the legacy system.
    m = MenuBar(
        a,
        {
            "foo": {
                "foo1": callback,
                "foo2": callback
            },
            "bar": {
                "bar1": callback,
                "bar2": callback
            }
        })

    assert m.master == a

    assert not callback_event.is_set()

    # menu invoke doesnt work...
    # m.tk.invoke(0)
    # assert callback_event.is_set()

    a.destroy()

def test_empty_menu():
    a = App()

    m = MenuBar(a)

    assert m.master == a

    a.destroy()
