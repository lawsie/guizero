from guizero import
import random


def read_sensor(app_obj, text_obj):
    sensor_value = random.randrange(3200, 5310, 10) / 100
    text_obj.set(sensor_value)
    app.update(1000, read_sensor, app_obj, text_obj)


if __name__ == '__main__':
    app = App(title='Sensor Display!',
              height=100,
              width=200,
              layout='grid')

    title = Text(app, 'Sensor value:', grid=[0, 0])
    text = Text(app, "xx", grid=[1, 0])

    app.update(1000, read_sensor, app, text)
    app.display()
