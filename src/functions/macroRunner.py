import time
import threading
import pynput
from ast import literal_eval
from src.functions.macroCommands import MacroCommands
import src.settings as settings
import src.constants as c


class MacroRunner:

    def __init__(self):
        self._script1_finish = False
        self._script2_finish = False
        self._escaped = False
    
    def reset(self):
        self._script1_finish = False
        self._script2_finish = False
        self._escaped = False

    # Runs the mouse click script and the rest of the script in parallel
    # This is to add a duration in mouse movement to its destination
    def runScript(self, script_array):
        print('you ran the script')
        print(script_array)
        self.listen()
        MacroRunner.compileScript(script_array)
        mouse_click_script, other_script = self.splitScript(script_array)
        mouse_click_script_thread = threading.Thread(
            target=self.runScriptParallel, args=(mouse_click_script, c.SCRIPT_TYPE_MOUSE_CLICK,)
        )
        other_script_thread = threading.Thread(
            target=self.runScriptParallel, args=(other_script, c.SCRIPT_TYPE_OTHER,)
        )
        mouse_click_script_thread.start()
        other_script_thread.start()
    
    # Wait for escaped to be pressed to interupt script
    def listen(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press)
        keyboard_listener.start()
    
    def on_press(self, key):
        if key == pynput.keyboard.Key.esc:
            # Check if already escaped
            if self._escaped:
                return
            print('you escaped')
            self._escaped = True
        return False

    # Seperate the mouse click component with the rest of the script
    @staticmethod
    def splitScript(script):
        mouse_click_script = []
        other_script = []
        for command in script:
            command_type = command[0]
            if command_type == 'on_click':
                mouse_click_script.append(command)
            else:
                other_script.append(command)
        return mouse_click_script, other_script
    
    def runScriptParallel(self, script, script_type):
        start_time = time.time()
        while script:
            if self._escaped:
                return
            end_time = time.time()
            time_passed = end_time - start_time
            command_time_next = float(script[0][1])
            if command_time_next < time_passed:
                MacroRunner.runCommand(script)
        self.checkFinished(script_type)

    def checkFinished(self, script_type):
        if script_type == c.SCRIPT_TYPE_MOUSE_CLICK:
            self._script1_finish = True
        elif script_type == c.SCRIPT_TYPE_OTHER:
            self._script2_finish = True
        
        if self._script1_finish and self._script2_finish:
            self._escaped = True
        print('Script finished')
        
    # Finds the command catagory and activates the corresponding function
    # options: 'on_click', 'on_scroll', 'on_press', 'on_hotkey'
    @staticmethod
    def runCommand(script):
        command = script.pop(0)
        command_type = command[0]
        command_time = command[1]
        if command_type == 'on_click':
            MacroRunner.run_on_click(command_time, command)
        elif command_type == 'on_scroll':
            MacroRunner.run_on_scroll(command_time, command)
        elif command_type == 'on_press':
            MacroRunner.run_on_press(command_time, command)
        elif command_type == 'on_hotkey':
            MacroRunner.run_on_hotkey(command_time, command)

    # Adjusts the numbers in the data stored in the csv file
    @staticmethod
    def compileScript(script_array):
        # Adjust the trigger time of on_click commands based on the DELAY required
        for command in script_array:
            if command[0] == 'on_click':
                trigger_time = float(command[1])
                adjusted_time = str(round(trigger_time - settings.DELAY, 2))
                command[1] = adjusted_time
        script_array.sort(key=lambda x:float(x[1]))

    """
    Converts the csv data into the correct data structure readable by pyautogui
    """

    @staticmethod
    def run_on_click(command_time, command):
        x = int(command[2])
        y = int(command[3])
        button = None
        if command[4] == 'Button.left':
            button = 'left'
        elif command[4] == 'Button.right':
            button = 'right'
        elif command[4] == 'Button.middle':
            button = 'middle'
        MacroCommands.command_click(command_time, x, y, button)
    
    @staticmethod
    def run_on_scroll(command_time, command):
        dx = command[2]
        dy = command[3]
        MacroCommands.command_scroll(command_time, dx, dy)
    
    @staticmethod
    def run_on_press(command_time, command):
        key = command[2]
        MacroCommands.command_press(command_time, key)

    @staticmethod
    def run_on_hotkey(command_time, command):
        keys = command[2]
        keys = literal_eval(keys)
        keys = list(keys)
        MacroCommands.command_hotkey(command_time, keys)
