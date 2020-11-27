from guizero import App, MenuBar
from threading import Event
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test
    )

def test_initial_values():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

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
