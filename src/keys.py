import keyboard
from time import sleep
def type_test(words):
    chars = words.split()

    for word in chars:
        for char in word:
            sleep(.05)
            keyboard.press_and_release(char)
        keyboard.press_and_release('spacebar')

