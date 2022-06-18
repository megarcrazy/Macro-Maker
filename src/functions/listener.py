import time
import pynput
from src.functions.scriptManager import ScriptManager


class Listener:

    def __init__(self):
        self._run = True
        self._script = []
        self._start_time = 0
        self._current_total_pressed = 0
        self._current_pressed_keys = []
    
    # Read mouse and keyboard input and start timer
    def listen(self):
        mouse_listener = pynput.mouse.Listener(
            on_click=self.on_click, on_scroll=self.on_scroll
        )
        keyboard_listener = pynput.keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        mouse_listener.start()
        keyboard_listener.start()
        self._start_time = time.time()
        print('record initiated')

    def on_click(self, x, y, button, pressed):
        if not self._run:
            return
        print(f'Mouse clicked at {x} {y} {button} {pressed}')
        if pressed:
            self._script.append(['on_click', self.get_time_passed(), x, y, button])

    def on_scroll(self, x, y, dx, dy):
        if not self._run:
            return
        print(f'Mouse scrolled at {x} {y} {dx} {dy}')
        self._script.append(['on_scroll', self.get_time_passed(), x, y, dx, dy])

    def on_press(self, key):
        if not self._run:
            return
        # If escape key detected, end listener
        if key == pynput.keyboard.Key.esc:
            self._run = False
            return
        print(f'Key pressed: {key}')
        self._current_total_pressed += 1
        parsed_key = self.parse_key(key)
        self._current_pressed_keys.append(parsed_key)
        
    def on_release(self, _):
        # Check if current pressed key array has been emptied to avoid repeat adding array
        if self._current_total_pressed == 0:
            return
        if self._current_total_pressed == 1:
            pressed_key = self._current_pressed_keys[0]
            self._script.append(['on_press', self.get_time_passed(), pressed_key])
        else:
            pressed_keys = self._current_pressed_keys
            self._script.append(['on_hotkey', self.get_time_passed(), pressed_keys])
        self._current_pressed_keys = []
        self._current_total_pressed = 0

    # Waits for escape to be pressed and saves the script in a csv file
    def wait_finish(self, url):
        self._script = []
        while self._run:
            time.sleep(0.1)
        # Store in temp file
        ScriptManager.saveScript(self._script, url)

    def get_time_passed(self):
        end_time = time.time()
        time_passed = round(end_time - self._start_time, 2)
        return time_passed

    # Converts key input from pynput into a human readable format
    # e.g. 'Key.alt_1' -> 'alt'
    @staticmethod
    def parse_key(key):
        parsed_key = str(key)   
        parsed_key = parsed_key.strip('\'')
        if '.' in parsed_key:
            parsed_key = parsed_key[parsed_key.find('.') + 1:]
        if 'alt' in parsed_key:
            parsed_key = 'alt'
        return parsed_key
