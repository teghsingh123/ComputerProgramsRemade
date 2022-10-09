from pynput.keyboard import Key,Listener
import pyautogui as pg

shiftcount = 0
altcount = 0
ctrlcount = 0

shift = None
alt = None
ctrl = None

def on_press(key):
    print("{0} pressed".format(
        key
    ))

def on_release(key):
    print("{0} released".format(
        key
    ))


    global shiftcount
    if key == Key.shift_l or key == Key.shift_r:
        shiftcount += 1

    global shift    
    if shiftcount % 3 == 1:
        shift = "single shift"
    elif shiftcount % 3 == 2:
        shift = "permanent shift"
    elif shiftcount % 3 == 0:
        shift = "shift not activated"

    if shift == "permanent shift":
        pg.keyDown("shift")


    global ctrlcount
    if key == Key.ctrl_l or key == Key.ctrl_r:
        ctrlcount += 1
    
    global ctrl   
    if ctrlcount % 3 == 1:
        ctrl = "single control"
    elif ctrlcount % 3 == 2:
        ctrl = "permanent control"
    elif ctrlcount % 3 == 0:
        ctrl = "control not activated"

    if ctrl == "permanent control":
        pg.keyDown("ctrl")

    global altcount
    if key == Key.alt_l or key == Key.alt_gr:
        altcount += 1

    global alt   
    if altcount % 3 == 1:
        alt = "single alt"
    elif altcount % 3 == 2:
        alt = "permanent alt"
    elif altcount % 3 == 0:
        alt = "alt not activated"

    if alt == "permanent alt":
        pg.keyDown("alt")

    if key == Key.esc:
        #print("Number of Shifts: " + str(shiftcount) + "\nNumber of Alts: " + str(altcount) + "\nNumber of Ctrls: " + str(ctrlcount))
        print(shift)
        print(alt)
        print(ctrl)
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()



