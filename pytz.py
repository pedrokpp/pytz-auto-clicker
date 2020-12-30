import pynput
import time
import threading
import os
import random
import colorama
from colorama import Fore, Back, Style
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
colorama.init()

os.system("title pytz clicker")
os.system("cls")

logo = r"""
               

          __ __     __  __    _______   _____     
         /_/\__/\ /\  /\  /\/\_______)\/\____\    
         ) ) ) ) )\ \ \/ / /\(___  __\/\/_ ( (    
        /_/ /_/ /  \ \__/ /   / / /       \ \_\   
        \ \ \_\/    \__/ /   ( ( (        / / /__ 
         )_) )      / / /     \ \ \      ( (____( 
         \_\/       \/_/      /_/_/       \/____/  v2
    
                    author: kp#3343
                                                                            

"""

print(Fore.RED + logo)
print(Style.RESET_ALL)
print(Fore.LIGHTRED_EX)
min_cps = float(input('   Min CPS: ')) 
max_cps = float(input('   Max CPS: '))
start_stop = input("   Start/Stop button  (Recommended: 'r'): ")
exitt = input("   Exit button  (Recommended: 'f'): ")
print("     KeyBind to start/stop the AC: " + start_stop)
print("     KeyBind to exit the AC: " + exitt)
print('         For more info about the AC like how too bypass, etc:')
print('                 https://discord.gg/cjSSY5c ') # not working anymore
button = Button.left
start_stop_key = KeyCode(char=start_stop) #mudar a bind pra iniciar e parar
exit_key = KeyCode(char=exitt) #mudar a bind pra dar exit
print(1/random.uniform(min_cps, max_cps))

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = 1/random.uniform(min_cps, max_cps)
        self.button = button
        self.running = False
        self.program_running = True
        
    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
                print(1/random.uniform(min_cps, max_cps))
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(1/random.uniform(min_cps, max_cps), button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()
