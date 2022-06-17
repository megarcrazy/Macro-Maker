from src.functions.scriptManager import ScriptManager
from src.functions.listener import Listener
import threading

def test_listen_script():
    listener = Listener()
    thread1 = threading.Thread(target=listener.listen)
    thread2 = threading.Thread(target=listener.wait_finish)
    thread1.start()
    thread2.start()

def test_load_script():
    ScriptManager.runScript(ScriptManager.loadScript())

test_listen_script()
# test_load_script()
