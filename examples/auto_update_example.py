from guizero import *
import random


def read_sensor():
    return random.randrange(3200, 5310, 10) / 100


def update_label():
    text.value = read_sensor()
    # recursive call
    text.after(1000, update_label)


if __name__ == '__main__':
    app = App(title='Sensor Display!',
              height=100,
              width=200,
              layout='grid')

    title = Text(app, 'Sensor value:', grid=[0, 0])
    text = Text(app, "xx", grid=[1, 0])

    text.after(1000, update_label)
    app.display()
