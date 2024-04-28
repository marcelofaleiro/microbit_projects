from microbit import *
import audio

timer = 0
display.show(Image(
    "00000:"
    "09090:"
    "00000:"
    "09990:"
    "00000"))
# audio.play(Sound.HELLO)

# Pseudo-random number generator


class SimpleRandom:
    def __init__(self, seed=0):
        self.seed = seed

    def random(self):
        self.seed = (self.seed * 1103515245 + 12345) & 0x7fffffff
        return self.seed / 0x7fffffff


# Perceptron parameters
learning_rate = 0.1
weights = [0.5, 0.5, 0.5, 0.5]  # Initialize weights
bias = 1

# Define activation function (step function)


def activate(sum):
    return 1 if sum >= 0 else 0


# Define training data for sound, light, and temperature predictions
training_data = [
    ([1023], 1),    # High sound
    ([0], 0),       # Low sound
    ([1023], 1),    # Bright light
    ([0], 0),       # Dark light
    ([35], 1),      # Hot temperature
    ([20], 0),      # Cold temperature
]

# Train the perceptron
random_generator = SimpleRandom()
for _ in range(1000):
    features, label = training_data[int(
        random_generator.random() * len(training_data))]
    sum = bias * weights[0] + features[0] * weights[1]
    prediction = activate(sum)
    error = label - prediction
    weights[0] += learning_rate * error * bias
    weights[1] += learning_rate * error * features[0]

while True:

    # Gather sensor data
    sound_level = microphone.sound_level()
    light_level = display.read_light_level()
    temp_c = temperature()

    # Make prediction for sound
    sum_sound = bias * weights[0] + sound_level * weights[1]
    prediction_sound = activate(sum_sound)

    # Make prediction for light
    sum_light = bias * weights[2] + light_level * weights[3]
    prediction_light = activate(sum_light)

    # Make prediction for temperature

    if button_b.was_pressed():
        timer = 0
        if temp_c > 35:
            sleep(100)
            prediction_temp = 1
        else:
            sleep(100)
            prediction_temp = 0

        # Display result
        if prediction_sound == 1:
            display.show(Image.MUSIC_QUAVERS)
            sleep(500)
        else:
            display.show(Image.ASLEEP)
            sleep(500)

        if prediction_light == 1:
            display.show(Image.HAPPY)
            sleep(500)
        else:
            display.show(Image.SAD)
            sleep(500)

        if prediction_temp == 1:
            display.show(Image.SKULL)
            sleep(500)
        else:
            display.show(Image.FABULOUS)
            sleep(500)

    if pin_logo.is_touched():
        timer = 0
        display.show(Image.GHOST)
        # audio.play(Sound.HAPPY)
    elif accelerometer.was_gesture('shake'):
        timer = 0
        display.show(Image.SURPRISED)
        # audio.play(Sound.GIGGLE)
    elif button_a.was_pressed():
        timer = 0
        display.scroll(temperature())
        sleep(500)
        display.show(Image.HAPPY)
        # audio.play(Sound.GIGGLE)
    else:
        sleep(500)
        timer += 0.5
        # sleep for half a second only to make it react more quickly to logo touch & shake

    if timer == 20:
        display.show(Image.SAD)
        # audio.play(Sound.SAD)
    elif timer == 300:
        display.show(Image.ASLEEP)
        # audio.play(Sound.YAWN)
