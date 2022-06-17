import pyautogui
import src.settings as settings


class MacroCommands:

    """
    Section for pyautogui output
    """

    @staticmethod
    def command_click(time, x, y, button):
        print(f'you {button} clicked at {time}s at {x} {y}')
        if not settings.TRIGGER_RUN:
            return
        if button is None:
            return
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(x=x, y=y, duration=settings.DELAY)
        pyautogui.click(button=button)

    @staticmethod
    def command_scroll(time, dx, dy):
        print(f'you scrolled {dx} {dy} at {time}s')
        if not settings.TRIGGER_RUN:
            return
        pyautogui.hscroll(dx)
        pyautogui.scroll(dy)

    @staticmethod
    def command_press(time, key):
        print(f'you pressed {key} at {time}s')
        if not settings.TRIGGER_RUN:
            return
        try:
            pyautogui.press(key)
        except:
            print("cannot find key")

    @staticmethod
    def command_hotkey(time, keys):
        print(f'you hotkeyed at {time}s')
        if not settings.TRIGGER_RUN:
            return
        try:
            pyautogui.hotkey(*keys)
        except:
            print("cannot find one of the keys")
