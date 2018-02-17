import sys
from guizero.utilities import convert_color

def do_color_conv(color):
    try:
        color = convert_color(color)
        print(color)
    except ValueError as e:
        print(e)
    except:
        print("Unexpected error:", sys.exc_info()[0])

do_color_conv("red")
do_color_conv("#000000")
do_color_conv((128,243,34))
do_color_conv((128,243))
do_color_conv(1)
