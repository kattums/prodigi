import sys
import time
import objc
from AppKit import NSWorkspace
import threading
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

ACTIVE_THRESHOLD_SECONDS = 5
active_time = 0
is_active = False

active_time_dict = {}

print(f"starting program on thread {threading.get_ident()}")

def event_handler():
    activepid = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier']
    activename = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    print(f'front pid is {activepid}')
    print(f'front process is {activename}')
    return

def receive_key_event(key):
    event_handler()
    return

def receive_mouse_event(x, y, button, pressed):
    if pressed:
        time.sleep(0.1)
        event_handler()
    return

# setup event listener threads
keyboard_listener = KeyboardListener(on_press=receive_key_event)
mouse_listener = MouseListener(on_click=receive_mouse_event)

# start threads and join them so script doesnt end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()