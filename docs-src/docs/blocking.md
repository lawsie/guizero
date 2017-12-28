## Loops and sleeping

You may be used to writing programs which contain loops or make use of the `sleep()` command, but find when you try to use these with guizero they cause your GUI to freeze. This is because guizero (in common with almost all GUIs) operates an **event driven** model of programming which may be different to the one you are familiar with.

Your first guizero program might look a bit like this:

```python
from guizero import App
app = App("Hello world")
app.display()
```

The line of code `app.display()` doesn't just display the app - it enters an **infinite event loop** which is watching and waiting for events to happen on the GUI. Events include things like the user clicking on a button, moving a slider, typing in a text box etc. No code written after this line will ever execute because the event loop is infinite.

### Example

Suppose you want a counter on your GUI to start counting up by 1 every second. You might be tempted to write a program like this:

```python
from guizero import App, Text
from time import sleep

app = App("Hello world")
text = Text(app, text="1")
while True:
    text.value = int(text.value) + 1
    sleep(1)
app.display()
```

If you run this program, you'll see that this does not have the desired effect - your program crashes! This is because you have blocked the updating of your GUI in two ways:

1. The `sleep()` command - whilst your program is sleeping, the GUI will not update and you will not be able to click on anything.

2. The `while` loop - once you enter this loop, your GUI will never update ever again and will probably crash.


### Solution

**This behaviour is not a bug within guizero or tkinter.**

You must write GUI based programs in a different way to the one you may be used to. If you want to repeatedly perform an action you would do it like this:

1. Write a function which performs the desired action (in this example `counter()`)

2. Set a **callback** to that function. You can either schedule the same callback to occur repeatedly after a given number of milliseconds (in this example `1000`), or you can schedule it only once.

```python
from guizero import App, Text

# Action you would like to perform
def counter():
    text.value = int(text.value) + 1

app = App("Hello world")
text = Text(app, text="1")
text.repeat(1000, counter)  # Schedule call to counter() every 1000ms
app.display()
```
