# Import necessary modules
from microbit import *
import utime

# Define function to check temperature and display result


# Set up event listener for button A press
while True:
    display.scroll(temperature())
    utime.sleep_ms(100) # Delay to prevent program from running too quickly
