import keyboard as kb
import pyautogui as pg
import time

class StickyKeys:
    def __init__(self):
        self.queue = []
        self.request()
    def request(self):
        self.key1 = kb.read_key()
        self.queue.append(self.key1)
        print(self.queue)
        time.sleep(0.5)
        self.key2 = kb.read_key()
        self.queue.append(self.key2)
        print(self.queue)
        self.exec()

    def exec(self):
        if self.check() == True:
            pg.keyDown(self.queue[0])
            pg.press(self.queue[1])
            pg.keyUp(self.queue[0])
        else:
            kb.press(self.queue[0] + "+" + self.queue[1])

    def check(self):    
        if 'alt' in self.queue or 'ctrl' in self.queue:
            return True
        

test = StickyKeys()