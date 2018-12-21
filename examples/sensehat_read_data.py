# An example showing how to use sensor data, here with the SenseHAT (or SenseHAT emulator)
# Refer to RaspberryPi forums Teaching and learning resources : https://www.raspberrypi.org/forums/viewtopic.php?f=49&t=202386 for some talk using it.
# compass added for show, but commented as it will not work if just enabled

from guizero import *
from sense_hat import SenseHat
# from sense_emu import SenseHat   #use this instead of sense_hat if you don't have a SenseHAT, but are using Raspbian/x86 Desktop

sense=SenseHat()

SENSOR_ENVIRONMENT_UPDATE_FREQUENCY = 1000  #time in milliseconds (ms)
SENSOR_IMU_UPDATE_FREQUENCY = 100

def read_temp_sensor():
    return round(sense.get_temperature(),1)

def read_humidity_sensor():
    return round(sense.get_humidity(),1)

def read_pressure_sensor():
    return round(sense.get_pressure()*0.1,1)


def update_environment_sensors():
    count_text.value=int(count_text.value)+1    #used to debug, i.e. check it is actually incrementing

    temperature_text.value = read_temp_sensor(),"°C"
    humidity_text.value = read_humidity_sensor(),"%"
    pressure_text.value = read_pressure_sensor(),"kPa"


def update_IMU_sensors():
    orient_yaw,orient_pitch,orient_roll = sense.get_orientation().values()
    mag_x,mag_y,mag_z = sense.get_compass_raw().values()
    acc_x,acc_y,acc_z = sense.get_accelerometer_raw().values()
    gyro_x,gyro_y,gyro_z = sense.get_gyroscope_raw().values()

    IMU_orient_yaw_text.value = round(orient_yaw,1)
    IMU_orient_pitch_text.value = round(orient_pitch,1)
    IMU_orient_roll_text.value = round(orient_roll,1)

    IMU_mag_x_text.value = round(mag_x,1)
    IMU_mag_y_text.value = round(mag_y,1)
    IMU_mag_z_text.value = round(mag_z,1)

    IMU_acc_x_text.value = round(acc_x,1)
    IMU_acc_y_text.value = round(acc_y,1)
    IMU_acc_z_text.value = round(acc_z,1)

    IMU_gyro_x_text.value = round(gyro_x,1)
    IMU_gyro_y_text.value = round(gyro_y,1)
    IMU_gyro_z_text.value = round(gyro_z,1)


if __name__ == '__main__':
    app = App(title="Sensor Display!",
              height=230,
              width=420,
              layout='grid')

    title_count = Text(app, "count 'debug':", grid=[0, 0])
    count_text = Text(app, "1", grid=[1, 0])


    title = Text(app, "Temperature Sensor value:", grid=[0, 1])
    temperature_text = Text(app, "xx", grid=[1, 1])

    title2 = Text(app, "Humidity Sensor value:", grid=[0, 2])
    humidity_text = Text(app, "xx", grid=[1, 2])

    title3 = Text(app, "Pressure Sensor value:", grid=[0, 3])
    pressure_text = Text(app, "xx", grid=[1, 3])

    #IMU box

    IMU_title_orient_yaw = Text(app, "Yaw", grid=[1, 5])
    IMU_title_orient_pitch = Text(app, "Pitch", grid=[2, 5])
    IMU_title_orient_roll = Text(app, "Roll", grid=[3, 5])

    IMU_title_orient = Text(app, "Orientation:", grid=[0, 6])
    IMU_orient_yaw_text = Text(app, "xx", grid=[1, 6])
    IMU_orient_pitch_text = Text(app, "xx", grid=[2, 6])
    IMU_orient_roll_text = Text(app, "xx", grid=[3, 6])

    IMU_title_x = Text(app, "X", grid=[1, 8])
    IMU_title_y = Text(app, "Y", grid=[2, 8])
    IMU_title_z = Text(app, "Z", grid=[3, 8])

    IMU_title_mag = Text(app, "Magnetometer µT", grid=[0, 9])
    IMU_title_acc = Text(app, "Accelerometer Gs", grid=[0, 10])
    IMU_title_gyro = Text(app, "Gyroscope rad/s", grid=[0, 11])

    IMU_mag_x_text = Text(app, "xx", grid=[1, 9])
    IMU_mag_y_text = Text(app, "xx", grid=[2, 9])
    IMU_mag_z_text = Text(app, "xx", grid=[3, 9])

    IMU_acc_x_text = Text(app, "xx", grid=[1, 10])
    IMU_acc_y_text = Text(app, "xx", grid=[2, 10])
    IMU_acc_z_text = Text(app, "xx", grid=[3, 10])

    IMU_gyro_x_text = Text(app, "xx", grid=[1, 11])
    IMU_gyro_y_text = Text(app, "xx", grid=[2, 11])
    IMU_gyro_z_text = Text(app, "xx", grid=[3, 11])

    IMU_title_compass = Text(app, "Compass North Bearing", grid=[0, 13])
    IMU_compass_text = Text(app, "xx", grid=[1, 13])

    app.repeat(SENSOR_ENVIRONMENT_UPDATE_FREQUENCY, update_environment_sensors)
    app.repeat(SENSOR_IMU_UPDATE_FREQUENCY, update_IMU_sensors)

    app.display()

