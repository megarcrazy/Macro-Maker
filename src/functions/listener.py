import time
import pynput
import threading
from src.functions.scriptManager import ScriptManager


class Listener:

    def __init__(self, window):
        self._window = window
        self._escaped = False
        self._script = []
        self._start_time = 0
        self._current_total_pressed = 0
        self._current_pressed_keys = []

    def run_listener(self):
        # Detect user input for mouse and keyboard
        thread1 = threading.Thread(target=self._listen)
        # Wait for listener to end and save script into a temporary file
        thread2 = threading.Thread(target=self._wait_finish, args=(self._window.get_temp_url(),))
        thread1.start()
        thread2.start()

    # Read mouse and keyboard input and start timer
    def _listen(self):
        mouse_listener = pynput.mouse.Listener(
            on_click=self._on_click, on_scroll=self._on_scroll
        )
        keyboard_listener = pynput.keyboard.Listener(
            on_press=self._on_press, on_release=self._on_release
        )
        mouse_listener.start()
        keyboard_listener.start()
        self._start_time = time.time()
        print('record initiated')
    
    # Waits for escape to be pressed and saves the script in a csv file
    def _wait_finish(self, url):
        self._script = []
        while not self._escaped:
            time.sleep(0.1)
        # Store in temp file
        ScriptManager.saveScript(self._script, url)
        self._window.change_status_record_escaped()

    def _on_click(self, x, y, button, pressed):
        if self._escaped:
            return
        print(f'Mouse clicked at {x} {y} {button} {pressed}')
        if pressed:
            self._script.append(['on_click', self._get_time_passed(), x, y, button])

    def _on_scroll(self, x, y, dx, dy):
        if self._escaped:
            return
        print(f'Mouse scrolled at {x} {y} {dx} {dy}')
        self._script.append(['on_scroll', self._get_time_passed(), x, y, dx, dy])

    def _on_press(self, key):
        if self._escaped:
            return
        # If escape key detected, end listener
        if key == pynput.keyboard.Key.esc:
            self._escaped = True
            return
        print(f'Key pressed: {key}')
        self._current_total_pressed += 1
        parsed_key = self._parse_key(key)
        self._current_pressed_keys.append(parsed_key)
        
    def _on_release(self, _):
        # Check if current pressed key array has been emptied to avoid repeat adding array
        if self._current_total_pressed == 0:
            return
        time_passed = self._get_time_passed()
        if self._current_total_pressed == 1:
            pressed_key = self._current_pressed_keys[0]
            self._script.append(['on_press', time_passed, pressed_key])
        else:
            pressed_keys = self._current_pressed_keys
            self._script.append(['on_hotkey', time_passed, pressed_keys])
        self._current_pressed_keys = []
        self._current_total_pressed = 0

    def _get_time_passed(self):
        end_time = time.time()
        time_passed = round(end_time - self._start_time, 2)
        return time_passed

    # Converts key input from pynput into a human readable format
    # e.g. 'Key.alt_1' -> 'alt'
    @staticmethod
    def _parse_key(key):
        parsed_key = str(key)   
        parsed_key = parsed_key.strip('\'')
        if '.' in parsed_key:
            parsed_key = parsed_key[parsed_key.find('.') + 1:]
        if 'alt' in parsed_key:
            parsed_key = 'alt'
        return parsed_key
