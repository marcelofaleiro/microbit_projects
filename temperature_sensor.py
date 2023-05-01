# Imports go at the top
from microbit import *

# Define the on_button_pressed_a function
def on_button_pressed_a():
    display.scroll(str(input.temperature()))

# Set up an event listener for when the A button is pressed
button_a.was_pressed = on_button_pressed_a

# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.ANGRY)
    sleep(1000)
    display.scroll('Hello')
