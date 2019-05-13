from guizero import App, Text, PushButton

def count_down():
    timer.value = int(timer.value) - 1
    if timer.value == "0":
        # cancel counter
        timer.cancel(count_down)
        # reset counter
        timer.value = 10
        # setup repeat
        timer.repeat(1000, count_down)

app = App("timer")

timer = Text(app, text="10")
timer.repeat(1000, count_down)

app.display()