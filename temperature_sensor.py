# Imports go at the top
from microbit import *

# Define the on_button_pressed_a function
def on_button_pressed_a():
    display.scroll(str(temperature()))

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.is_pressed():
        on_button_pressed_a()
    display.show(Image.ANGRY)
    sleep(1000)
